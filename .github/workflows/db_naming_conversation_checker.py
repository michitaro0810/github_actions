import re
from spellchecker import SpellChecker
import os
import subprocess
import sys
import spacy
import random
from spacy.matcher import Matcher
import nltk
from nltk.stem import WordNetLemmatizer
nltk.download('wordnet')

args = sys.argv
spell = SpellChecker()
pr_number = os.environ['PR_NUMBER']
github_users = ['@test1','@test2','@test3','@test4']

#スネークケースチェッカー(大文字を使わないことを含む)
def is_snakecase(target_string):
    # スネークケースが全体的に小文字かどうかをチェック
    if not target_string.islower():
        # print(target_string + " ← 文字列全体が小文字になっています")
        return False

    #_(アンダーバー)ごとに区切り, スペルチェックをする
    else:
        splited_list = target_string.split('_')
        misspelled = spell.unknown(splited_list)
        if len(misspelled) > 0:
            # print(target_string + " ← キャメルケースになっていますが，単語が正しく区切られていないか，スペルミスがあります")
            return False
        else:
            # print("正常なキャメルケースになっています")
            return True

#複数形かどうかのチェッカー
def is_plural(word):
    lemmatizer = WordNetLemmatizer()
    lemma = lemmatizer.lemmatize(word, 'n')
    return word != lemma

#スネークケースかつすべて複数形の場合
def is_all_plural_snakecase(target_string):
    if not is_snakecase(target_string):
        return False
    words = target_string.split('_')
    #all()関数はすべての結果がtrueであればtrueで帰ってくる
    return all(is_plural(word) for word in words)


#スネークケースかつすべて単数の場合
def is_all_singular_snakecase(target_string):
    if not is_snakecase(target_string):
        return False
    words = target_string.split('_')
    #all()関数はすべての結果がtrueであればtrueで帰ってくる
    return all(not is_plural(word) for word in words)


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
            if not is_snakecase(line[4:][:-1]):
                print(str(num) +"行目の " + line[4:][:-1] +" がスネークケースになっていません")
                has_error = True
                subprocess.call('gh pr review ' + str(pr_number) + ' -r -b "' + str(num) +"行目のテーブル名 " + line[4:][:-1] +' がスネークケースになっていません \n ' + github_users[random_number_1] + 'さん，' + github_users[random_number_2] + 'さん，1つ目に何の規則を間違えて利用していたか, 2つ目に識別子の認識のミスか, 規則の認識のミスなのか, 3つ目に正しい命名規則としてなにを用いるべきかをQuote replyで記入してください．"', shell=True)
            if not is_all_plural_snakecase(line[4:][:-1]):
                print(str(num) +"行目の " + line[4:][:-1] +" が複数形になっていません")
                has_error = True
                subprocess.call('gh pr review ' + str(pr_number) + ' -r -b "' + str(num) +"行目のテーブル名 " + line[4:][:-1] +' が複数形になっていません \n ' + github_users[random_number_1] + 'さん，' + github_users[random_number_2] + 'さん，1つ目に何の規則を間違えて利用していたか, 2つ目に識別子の認識のミスか, 規則の認識のミスなのか, 3つ目に正しい命名規則としてなにを用いるべきかをQuote replyで記入してください．"', shell=True)
        if not line.startswith("|") and field_flag:
            field_flag = False
        if line.startswith("|フィールド名"):
            field_flag = True
        if  line.startswith("|:"):
            continue
        if line.startswith("|") and not line.startswith("|フィールド名") and field_flag:
            if not is_snakecase(line[1:].split('|')[0]):
                has_error = True
                print(str(num) +"行目の " + line[1:].split('|')[0] +" がスネークケースになっていません")
                subprocess.call('gh pr review ' + str(pr_number) + ' -r -b "' + str(num) +"行目のフィールド名 " + line[1:].split('|')[0] +' がスネークケースになっていません\n ' + github_users[random_number_1] + 'さん，' + github_users[random_number_2] + 'さん，1つ目に何の規則を間違えて利用していたか, 2つ目に識別子の認識のミスか, 規則の認識のミスなのか, 3つ目に正しい命名規則としてなにを用いるべきかをQuote replyで記入してください．"', shell=True)
            if not is_all_singular_snakecase(line[1:].split('|')[0]):
                has_error = True
                print(str(num) +"行目の " + line[1:].split('|')[0] +" が単数になっていません")
                subprocess.call('gh pr review ' + str(pr_number) + ' -r -b "' + str(num) +"行目のフィールド名 " + line[1:].split('|')[0] +' がスネークケースになっていません\n ' + github_users[random_number_1] + 'さん，' + github_users[random_number_2] + 'さん，1つ目に何の規則を間違えて利用していたか, 2つ目に識別子の認識のミスか, 規則の認識のミスなのか, 3つ目に正しい命名規則としてなにを用いるべきかをQuote replyで記入してください．"', shell=True)

if not has_error:
        subprocess.call('gh pr review ' + str(pr_number) + ' -a -b "命名規則エラーは見つかりませんでした"', shell=True)