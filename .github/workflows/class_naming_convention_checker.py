import re
from spellchecker import SpellChecker
import os
import subprocess
import sys

args = sys.argv
spell = SpellChecker()
pr_number = os.environ['PR_NUMBER']
#キャメルケースになっているかチェックする場合
def is_cammelcase(target_string):
    #まずスネークケースになっていないかチェック
    if "_" in target_string:
        # print(target_string + " ← アンダーバーが含まれています，スネークケースになっていませんか？")
        return False
    #次に最初の文字が大文字になっていないかチェック
    elif target_string[0].isupper():
        # print(target_string + " ← 先頭の文字が大文字になっています")
        return False
    #最後に，大文字で正しく単語が区切られているかチェック
    else:
        splited_list = re.split('(?=[A-Z])', target_string)
        misspelled = spell.unknown(splited_list)
        if len(misspelled) > 0:
            # print(target_string + " ← キャメルケースになっていますが，単語が正しく区切られていないか，スペルミスがあります")
            return False
        else:
            # print("正常なキャメルケースになっています")
            return True

def is_pascalcase(target_string):
    #まずスネークケースになっていないかチェック
    if "_" in target_string:
        # print(target_string + " ← アンダーバーが含まれています，スネークケースになっていませんか？")
        return False
    #次に最初の文字が大文字になっていないかチェック
    elif not target_string[0].isupper():
        # print(target_string + " ← 先頭の文字が小文字になっています")
        return False
    #最後に，大文字で正しく単語が区切られているかチェック
    else:
        splited_list = re.split('(?=[A-Z])', target_string)
        splited_list.remove("")
        # print(splited_list)
        misspelled = spell.unknown(splited_list)
        if len(misspelled) > 0:
            # print(target_string + " ← パスカルケースになっていますが，単語が正しく区切られていないか，スペルミスがあります")
            return False
        else:
            # print("正常なパスカルケースになっています")
            return True
    
def is_date(target_string):
        if target_string.endswith("On"):
            return True
        else:
            return False
        
def is_datetime(target_string):
        if target_string.endswith("At"):
            return True
        else:
            return False
    
        
#test start
# is_cammelcase("snake_case")
# is_cammelcase("UpperCamelCase")
# is_cammelcase("lowerCamelCasse")
# is_cammelcase("lowerCamelId")
# is_pascalcase("Book")
print(args[1])
with open(args[1]) as f:
    has_error = False
    num = 0
    field_flag = False
    for line in f:
        print(line)
        num += 1
        if line.startswith("###"):
            # print(line[4:][:-1])
            if not is_pascalcase(line[4:][:-1]):
                print(str(num) +"行目の " + line[4:][:-1] +" がパスカルケースになっていません")
                has_error = True
                subprocess.call('gh pr review ' + str(pr_number) + ' -r -b "' + str(num) +"行目のクラス名 " + line[4:][:-1] +' がパスカルケースになっていません"', shell=True)
        if not line.startswith("|") and field_flag:
            field_flag = False
        if line.startswith("|フィールド名"):
            field_flag = True
        if  line.startswith("|:"):
            continue
        if line.startswith("|") and not line.startswith("|フィールド名") and field_flag:
            if not is_cammelcase(line[1:].split('|')[0]):
                has_error = True
                print(str(num) +"行目の " + line[1:].split('|')[0] +" がキャメルケースになっていません")
                subprocess.call('gh pr review ' + str(pr_number) + ' -r -b "' + str(num) +"行目のフィールド名 " + line[1:].split('|')[0] +' がキャメルケースになっていません"', shell=True)
            if line[1:].split('|')[3] == "date" or line[1:].split('|')[3] == "Date":
                if not is_date(line[1:].split('|')[0]):
                    has_error = True
                    print(str(num) +"行目の " + line[1:].split('|')[0] +" の日付型のフィールド名末尾がOnになっていません")
                    subprocess.call('gh pr review ' + str(pr_number) + ' -r -b "' + str(num) +"行目のフィールド名 " + line[1:].split('|')[0] +'の日付型のフィールド名末尾がOnになっていません"', shell=True)
            if line[1:].split('|')[3] == "datetime" or line[1:].split('|')[3] == "Datetime" or line[1:].split('|')[3] == "DateTime":
                if not is_datetime(line[1:].split('|')[0]):
                    has_error = True
                    print(str(num) +"行目の " + line[1:].split('|')[0] +" の日時型のフィールド名末尾がAtになっていません")
                    subprocess.call('gh pr review ' + str(pr_number) + ' -r -b "' + str(num) +"行目のフィールド名 " + line[1:].split('|')[0] +'の日付型のフィールド名末尾がOnになっていません"', shell=True)
    if not has_error:
        subprocess.call('gh pr review ' + str(pr_number) + ' -a -b "命名規則エラーは見つかりませんでした"', shell=True)