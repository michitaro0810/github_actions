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
# pr_number = 1
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

#スネークケースかつ最後の単語が複数形の場合
def is_all_plural_snakecase(target_string):
    if not is_snakecase(target_string):
        return False
    words = target_string.split('_')
    for word in words:
        if is_plural(word):
            return True
    return False


#スネークケースかつすべて単数の場合
def is_all_singular_snakecase(target_string):
    if not is_snakecase(target_string):
        return False
    words = target_string.split('_')
    #all()関数はすべての結果がtrueであればtrueで帰ってくる
    return all(not is_plural(word) for word in words)

def is_date(target_string):
        if target_string.endswith("_on"):
            return True
        else:
            return False
        
def is_datetime(target_string):
        if target_string.endswith("_at"):
            return True
        else:
            return False

def snake_tokenizer(target_string):
    splited_list = re.split('_', target_string)
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
    if target_string.startswith("is") or target_string.startswith("has") or is_3rd_person_singular_verb(snake_tokenizer(target_string)[0]):
        return True
    else:
        return False

# print(args[1])
with open(args[1]) as f:
    has_error = False
    num = 0
    field_flag = False
    for line in f:
        # print(line)
        num += 1
        while True:
            random_number_1 = random.randint(0, 3)
            random_number_2 = random.randint(0, 3)
            if random_number_1 != random_number_2:
                break
        if line.startswith("###"):
            print(line[4:][:-1])
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
        if line.startswith("|カラム名"):
            field_flag = True
            # print(line)
        if line.startswith("|:"):
            continue
        if line.startswith("|") and not line.startswith("|カラム名") and field_flag:
            # print(line)
            if not is_snakecase(line[1:].split('|')[0]):
                has_error = True
                print(str(num) +"行目の " + line[1:].split('|')[0] +" がスネークケースになっていません")
                subprocess.call('gh pr review ' + str(pr_number) + ' -r -b "' + str(num) +"行目のカラム名 " + line[1:].split('|')[0] +' がスネークケースになっていません\n ' + github_users[random_number_1] + 'さん，' + github_users[random_number_2] + 'さん，1つ目に何の規則を間違えて利用していたか, 2つ目に識別子の認識のミスか, 規則の認識のミスなのか, 3つ目に正しい命名規則としてなにを用いるべきかをQuote replyで記入してください．"', shell=True)
            elif not is_all_singular_snakecase(line[1:].split('|')[0]) and not (line[1:].split('|')[2] == "boolean" or line[1:].split('|')[2] == "Boolean" or line[1:].split('|')[2] == "bool") :
                has_error = True
                print(str(num) +"行目の " + line[1:].split('|')[0] +" が単数になっていません")
                subprocess.call('gh pr review ' + str(pr_number) + ' -r -b "' + str(num) +"行目のカラム名 " + line[1:].split('|')[0] +' がスネークケースになっていません\n ' + github_users[random_number_1] + 'さん，' + github_users[random_number_2] + 'さん，1つ目に何の規則を間違えて利用していたか, 2つ目に識別子の認識のミスか, 規則の認識のミスなのか, 3つ目に正しい命名規則としてなにを用いるべきかをQuote replyで記入してください．"', shell=True)
            if line[1:].split('|')[2] == "date" or line[1:].split('|')[2] == "Date":
                if not is_date(line[1:].split('|')[0]):
                    has_error = True
                    print(str(num) +"行目の " + line[1:].split('|')[0] +" の日付型のカラム名末尾がonになっていません")
                    subprocess.call('gh pr review ' + str(pr_number) + ' -r -b "' + str(num) +"行目のカラム名 " + line[1:].split('|')[0] +'の日付型のカラム名末尾がonになっていません\n ' + github_users[random_number_1] + 'さん，' + github_users[random_number_2] + 'さん，このミスが生じた原因と，修正方法をQuote replyで記入してください．"', shell=True)
            if line[1:].split('|')[2] == "datetime" or line[1:].split('|')[2] == "Datetime" or line[1:].split('|')[2] == "DateTime":
                if not is_datetime(line[1:].split('|')[0]):
                    has_error = True
                    print(str(num) +"行目の " + line[1:].split('|')[0] +" の日時型のカラム名末尾がatになっていません")
                    subprocess.call('gh pr review ' + str(pr_number) + ' -r -b "' + str(num) +"行目のカラム名 " + line[1:].split('|')[0] +'の日時型のカラム名末尾がatになっていません\n ' + github_users[random_number_1] + 'さん，' + github_users[random_number_2] + 'さん，このミスが生じた原因と，修正方法をQuote replyで記入してください．"', shell=True)
            if line[1:].split('|')[2] == "boolean" or line[1:].split('|')[2] == "Boolean" or line[1:].split('|')[2] == "bool":
                if not is_boolean(line[1:].split('|')[0]):
                    has_error = True
                    print(str(num) +"行目の " + line[1:].split('|')[0] +" の真偽値型のカラム名がis,has,三単現動詞で始まっていません")
                    subprocess.call('gh pr review ' + str(pr_number) + ' -r -b "' + str(num) +"行目のカラム名 " + line[1:].split('|')[0] +'の真偽値型のカラム名がis,has,三単現動詞で始まっていません\n ' + github_users[random_number_1] + 'さん，' + github_users[random_number_2] + 'さん，このミスが生じた原因と，修正方法をQuote replyで記入してください．"', shell=True)
if not has_error:
        subprocess.call('gh pr review ' + str(pr_number) + ' -a -b "命名規則エラーは見つかりませんでした"', shell=True)
