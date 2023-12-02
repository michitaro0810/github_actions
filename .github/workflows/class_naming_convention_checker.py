import re
from spellchecker import SpellChecker
import os
import subprocess
import sys
import spacy
import random
from spacy.matcher import Matcher

args = sys.argv
spell = SpellChecker()
pr_number = os.environ['PR_NUMBER']
github_users = ['@test1','@test2','@test3','@test4']
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
def camel_tokenizer(target_string):
    splited_list = re.split('(?=[A-Z])', target_string)
    return splited_list

def lowerer(target_list):
    return list(map(lambda x: x.lower(), target_list))

def is_3rd_person_singular_verb(word):
    # spaCyの英語モデルをロード
    nlp = spacy.load("en_core_web_sm")
    # "He"が付いた文を作成
    text = f"He {word}"
    # spaCyのドキュメントオブジェクトを取得
    doc = nlp(text)
    # Matcherを初期化
    matcher = Matcher(nlp.vocab)
    # カスタムルールを追加
    pattern = [{"POS": "PRON", "lower": "he"}, {"POS": "VERB", "tag": "VBZ"}]
    matcher.add("3rd_person_singular", [pattern])
    # Matcherを適用
    matches = matcher(doc)
    # マッチがあれば三単現動詞とみなす
    return bool(matches)

def is_boolean(target_string):
    if target_string.startswith("is") or target_string.startswith("has") or is_3rd_person_singular_verb(camel_tokenizer(target_string)[0]):
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
        while True:
            random_number_1 = random.randint(0, 3)
            random_number_2 = random.randint(0, 3)
            if random_number_1 != random_number_2:
                break
        if line.startswith("###"):
            # print(line[4:][:-1])
            if not is_pascalcase(line[4:][:-1]):
                print(str(num) +"行目の " + line[4:][:-1] +" がパスカルケースになっていません")
                has_error = True
                subprocess.call('gh pr review ' + str(pr_number) + ' -r -b "' + str(num) +"行目のクラス名 " + line[4:][:-1] +' がパスカルケースになっていません \n ' + github_users[random_number_1] + 'さん，' + github_users[random_number_2] + 'さん，このミスが生じた原因と，修正方法をQuote replyで記入してください．"', shell=True)
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
                subprocess.call('gh pr review ' + str(pr_number) + ' -r -b "' + str(num) +"行目のフィールド名 " + line[1:].split('|')[0] +' がキャメルケースになっていません\n ' + github_users[random_number_1] + 'さん，' + github_users[random_number_2] + 'さん，このミスが生じた原因と，修正方法をQuote replyで記入してください．"', shell=True)
            if line[1:].split('|')[2] == "date" or line[1:].split('|')[2] == "Date":
                print("date")
                if not is_date(line[1:].split('|')[0]):
                    has_error = True
                    print(str(num) +"行目の " + line[1:].split('|')[0] +" の日付型のフィールド名末尾がOnになっていません")
                    subprocess.call('gh pr review ' + str(pr_number) + ' -r -b "' + str(num) +"行目のフィールド名 " + line[1:].split('|')[0] +'の日付型のフィールド名末尾がOnになっていません\n ' + github_users[random_number_1] + 'さん，' + github_users[random_number_2] + 'さん，このミスが生じた原因と，修正方法をQuote replyで記入してください．"', shell=True)
            if line[1:].split('|')[2] == "datetime" or line[1:].split('|')[2] == "Datetime" or line[1:].split('|')[2] == "DateTime":
                print("datetime")
                print(line[1:].split('|')[0])
                print(is_datetime(line[1:].split('|')[0]))
                if not is_datetime(line[1:].split('|')[0]):
                    has_error = True
                    print(str(num) +"行目の " + line[1:].split('|')[0] +" の日時型のフィールド名末尾がAtになっていません")
                    subprocess.call('gh pr review ' + str(pr_number) + ' -r -b "' + str(num) +"行目のフィールド名 " + line[1:].split('|')[0] +'の日時型のフィールド名末尾がAtになっていません\n ' + github_users[random_number_1] + 'さん，' + github_users[random_number_2] + 'さん，このミスが生じた原因と，修正方法をQuote replyで記入してください．"', shell=True)
            if line[1:].split('|')[2] == "boolean" or line[1:].split('|')[2] == "Boolean" or line[1:].split('|')[2] == "bool":
                print("datetime")
                print(line[1:].split('|')[0])
                print(is_boolean(line[1:].split('|')[0]))
                if not is_boolean(line[1:].split('|')[0]):
                    has_error = True
                    print(str(num) +"行目の " + line[1:].split('|')[0] +" の真偽値型のフィールド名がis,has,三単現動詞で始まっていません")
                    subprocess.call('gh pr review ' + str(pr_number) + ' -r -b "' + str(num) +"行目のフィールド名 " + line[1:].split('|')[0] +'の真偽値型のフィールド名がis,has,三単現動詞で始まっていません\n ' + github_users[random_number_1] + 'さん，' + github_users[random_number_2] + 'さん，このミスが生じた原因と，修正方法をQuote replyで記入してください．"', shell=True)
    if not has_error:
        subprocess.call('gh pr review ' + str(pr_number) + ' -a -b "命名規則エラーは見つかりませんでした"', shell=True)