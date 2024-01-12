# DB設計書SEG1

## データベース名: schoolapp_db
---
## 改版履歴
|発行日|版数|改版内容|
|:--|:--|:--|
|2021/11/23|1.0|初版|
|2021/12/01|1.1|第2版 テーブル名の変更、「作成日」項目の変更、欠席の変数の型をbooleanに変更、座席を通し番号に変更|
|2021/12/06|1.2|第3版 テーブル名にカラム名を追記、lessonsに座席配置IDを追記、システム上で設定されるID（classes,members,seating_arrangements,students_seating_arrangements,grades,lessons）の制約にAUTO_INCREMENTを追記|
|2021/12/06|2.0|第4版 外部キーの制約を追加、開始期間&終了期間のYYYY部分に格納する要素の明記、座席位置の制約を統一

---

## テーブル一覧

<br>


<br>

テーブル名:
### user
（ユーザー）
|カラム名|型|長さ|主キー|NULL|制約|概要|備考|
|:--|:--|:--|:--|:--|:--|:--|:--|
|id||varchar|15|YES|NO|半角英数字のみ（6文字以上15文字以下）|ユーザーID|重複なし|
|password||varchar|64|NO|NO|8文字以上15文字以下の文字列	半角英数字のみで構成され、英字・数字をそれぞれ1つ以上含む|パスワード|ハッシュ化したもの|

<br>

テーブル名:
### students
（生徒）
|カラム名|型|長さ|主キー|NULL|制約|概要|備考|
|:--|:--|:--|:--|:--|:--|:--|:--|
|id||varchar|15|YES|NO|半角英数字のみ（6文字以上15文字以下）|生徒ID|重複なし 児童・生徒を一意に決める文字列|
|gender||integer||NO|NO|1:男 2:女 3:その他|性別|女、男、その他から選択.席では女は赤、男は青,その他は灰色の背景になる|
|name||varchar|20|NO|NO|1文字以上20文字以下|氏名||
|user_id||varchar|15|NO|NO|半角英数字のみ（6文字以上15文字以下)|ユーザーID(管理教員ID)|外部キー|


テーブル名：
### classes
（クラス）
|カラム名|型|長さ|主キー|NULL|制約|概要|備考|
|:--|:--|:--|:--|:--|:--|:--|:--|
|id||integer||YES|NO|AUTO_INCREMENT|クラスID|
|name||varchar|20|NO|NO|1文字以上20文字以下|クラス名|
|year||integer||NO|NO|数字4桁|年度|
|user_id||varchar|15|NO|NO|半角英数字のみ（6文字以上15文字以下)|ユーザーID（管理教員ID）|外部キー|


テーブル名：
### members
（メンバー）
|カラム名|型|長さ|主キー|NULL|制約|概要|備考|
|:--|:--|:--|:--|:--|:--|:--|:--|
|id||integer||YES|NO|AUTO_INCREMENT||
|class_id||integer||NO|NO||クラスID|外部キー|
|student_id||varchar|15|NO|NO|半角英数字のみ（6文字以上15文字以下）|生徒ID|外部キー|


テーブル名：
### seating_arrangements
（座席配置）
|カラム名|型|長さ|主キー|NULL|制約|概要|備考|
|:--|:--|:--|:--|:--|:--|:--|:--|
|id||integer||YES|NO|AUTO_INCREMENT|座席配置ID|
|class_id||integer||NO|NO||クラスID|外部キー|
|created_date||date||NO|NO||作成日||
|start_date||date||NO|NO|クラスの年度から算出した年と月と日付|開始期間|
|end_date||date||NO|YES|クラスの年度から算出した年と月と日付|終了期間|
|name||varchar|20|NO|YES|0文字以上20文字以下の文字列|座席配置名||
|user_id||varchar|15|NO|NO|半角英数字のみ（6文字以上15文字以下)|ユーザーID（管理教員ID）|外部キー

テーブル名：
### students_seating_arrangements
（座席）
|カラム名|型|長さ|主キー|NULL|制約|概要|備考|
|:--|:--|:--|:--|:--|:--|:--|:--|
|id|integer||YES|NO|AUTO_INCREMENT|生徒と座席の関連ID||
|seating_arrangements_id|integer||NO|NO||座席配置ID|
|student_id|varchar|15|NO|NO|半角英数字のみ（6文字以上15文字以下）|生徒ID|
|seat|integer||NO|NO|1~42の通し番号|座席|


テーブル名：
### grades
（評価）
|カラム名|型|長さ|主キー|NULL|制約|概要|備考|
|:--|:--|:--|:--|:--|:--|:--|:--|
|id||integer||YES|NO|AUTO_INCREMENT|評価ID|
|student_id||varchar||NO|NO|半角英数字のみ（6文字以上15文字以下|生徒ID|外部キー
|lesson_id||integer||NO|NO||授業ID|外部キー|
|attendance||boolean||NO|NO|0:欠席1:出席|出欠|
|red||integer||NO|YES|1:A 2:B 3:C|観点１|
|green||integer||NO|YES|1:A 2:B 3:C|観点２|
|blue||integer||NO|YES|1:A 2:B 3:C|観点３|
|comment||varchar|400|NO|YES|0文字以上400文字以下の文字列|評価のコメント|生徒個人の評価|
|seat||integer||NO|NO|1~42の通し番号|座席||
|user_id||varchar|15|NO|NO|半角英数字のみ（6文字以上15文字以下)|ユーザーID（管理教員ID）|外部キー

テーブル名：
### lessons（授業）
|カラム名|型|長さ|主キー|NULL|制約|概要|備考|
|:--|:--|:--|:--|:--|:--|:--|:--|
|id||integer||YES|NO|AUTO_INCREMENT|授業ID|
|seating_arrangements_id||integer||NO|NO||座席配置ID|外部キー
|lesson_date||date||NO|NO||授業日||
|period_num||integer||NO|NO||時限|1~6限を想定|
|comment||varchar||NO|NO|0文字以上400文字以下の文字列|評価のコメント|授業コメント|授業全体へのコメント|



