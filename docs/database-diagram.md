# 2020年度シスプロG2 データベース設計図

## 改版履歴

|発行日|版数|改版内容|担当|
|:--:--|:---|::--:--:--:--:--:--|:---|
020/12/02.0|初版の作成|渡邊|
020/12/04.0|全体での最終確認　指摘部分の修正|渡邊|
020/12/04.1|gradeをENUM型に変更,cooksテーブル3,4をNULL許容に変更,及び誤字修正|上岡|
020/12/07.0|インスペクションを受けての修正|上岡|
020/12/15.0|インスペクションを受けての修正<br>予め格納しておくデータの追記|久保|
020/12/15.0|テーブル名をclasses→school_classesに変更|久保|


***
## データベース名　menus
</br>

## テーブル一覧

### users

|カラム名||型|長さ|主キー|NULL|制約|概要|備考|
|:--|:--|:--|:--|:--|:--|:--|:--|:--|
|id||VARCHAR6|YES|NO|なし|ログイン時のid||
|name||VARCHAR4|NO|NO|なし|ユーザ名||
|password||VARCHAR55|NO|NO|なし|パスワード|ハッシュ化|
|grade||ENUM||NO|NO|なし|学年(小5,6 中1,2,3 高1,2,3)||
|sex||INT||NO|NO||性別(男1,女2)||
|school_class_id||INT||NO|NO|school_class/idの外部キー, デフォルト:0|所属するクラスid||

### teachers
|カラム名||型|長さ|主キー|NULL|制約|概要|備考|
|:--|:--|:--|:--|:--|:--|:--|:--|:--|
|id||VARCHAR6|YES|NO|なし|ログイン時のid||
|name||VARCHAR4|NO|NO|なし|教師名||
|password||VARCHAR55|NO|NO|なし|パスワード|ハッシュ化|

### school_classes
|カラム名||型|長さ|主キー|NULL|制約|概要|備考|
|:--|:--|:--|:--|:--|:--|:--|:--|:--|
|id||INT||YES|NO|Autoincrement|クラスid||
|title||VARCHAR4|NO|NO|なし|クラスタイトル||
|key||VARCHAR55|NO|NO|Uniqueキー|クラスの認証キー|ハッシュ化|
|teacher_id||VARCHAR6|NO|NO|teacher/idの外部キー|作成した教員のid||
|cook_id||INT||NO|NO|cooks/idの外部キー, デフォルト:1|事前設定された献立id||

### cooks
|カラム名||型|長さ|主キー|NULL|制約|概要|備考|
|:--|:--|:--|:--|:--|:--|:--|:--|:--|
|id||INT||YES|NO|Autoincrement|献立id||
|name||VARCHAR4|NO|NO|なし|献立名||
|teacher_id||VARCHAR6|NO|YES|teacher/idの外部キー|作成した教師id3に値が入った場合, No.4はNULL|
|user_id||VARCHAR6|NO|YES|user/idの外部キー|作成した生徒id4に値が入った場合, No.3はNULL|
|created_at||DATETIME||NO|NO|なし|献立作成の日時||
|user_grade||ENUM||NO|NO|小5,6 中1,2,3 高1,2,3と教員(教員用※)の9つのどれか|作成時の学年||

***※教員が作成した献立の場合, user_gradeにnullを入れるのではなく教員用の列挙子を用意することで対応したい***


### cook_menus
|カラム名||型|長さ|主キー|NULL|制約|概要|備考|
|:--|:--|:--|:--|:--|:--|:--|:--|:--|
|id||INT||YES|NO|Autoincrement|id||
|is_breakfast||BOOLEAN||NO|NO|デフォルト:0|献立が朝食かどうか|朝食の調理品なら1|
|is_lunch||BOOLEAN||NO|NO|デフォルト:0|献立が昼食かどうか|昼食の調理品なら1|
|is_dinner||BOOLEAN||NO|NO|デフォルト:0|献立が夕食かどうか|夕食の調理品なら1|
|is_snack||BOOLEAN||NO|NO|デフォルト:0|献立が間食かどうか|間食の調理品なら1|
|cook_id||INT||NO|NO|cook/idの外部キー|献立id||
|menu_id||INT||NO|NO|menu/idの外部キー|調理品id||


### menus
|カラム名||型|長さ|主キー|NULL|制約|概要|備考|
|:--|:--|:--|:--|:--|:--|:--|:--|:--|
|id||INT||YES|NO|Autoincrement|調理品id||
|name||VARCHAR55|NO|NO|なし|調理品名||
|created_at||DATETIME||NO|NO|なし|作成日||
|updated_at||DATETIME||NO|NO|なし|更新日|自動更新|
|menu_category_id||INT||NO|NO|menu_category/idの外部キー|調理品カテゴリーid||

### menu_categorys
|カラム名||型|長さ|主キー|NULL|制約|概要|備考|
|:--|:--|:--|:--|:--|:--|:--|:--|:--|
|id||INT||YES|NO|Autoincrement|調理品カテゴリーid||
|name||VARCHAR55|NO|NO|なし|カテゴリー名||
|created_at||DATETIME||NO|NO|なし|作成日||
|updated_at||DATETIME||NO|NO|なし|更新日|自動更新|

### menu_ingredients
|カラム名||型|長さ|主キー|NULL|制約|概要|備考|
|:--|:--|:--|:--|:--|:--|:--|:--|:--|
|id||INT||YES|NO|Autoincrement|||
|quantity||INT||NO|NO|なし|||
|menu_id||INT||NO|NO|menu/idの外部キー|調理品id||
|ingredient_id||INT||NO|NO|ingredient/idの外部キー|材料および栄養素id||

### ingredients
|カラム名||型|長さ|主キー|NULL|制約|概要|備考|
|:--|:--|:--|:--|:--|:--|:--|:--|:--|
|id||INT||YES|NO|Autoincrement|材料および栄養素id||
|group_id||INT||NO|NO|なし|グループid||
|name||VARCHAR55|NO|NO|なし|メニュー名||
|以下略||||||||

<br>

### 予め格納しておくデータ  

各テーブルの外部キーには，```not null```制約がかけられている．  
よって，いくつかのテーブルに予めデータを格納しておく必要があるので，その内容を記載する．

* teachers  

|カラム名||id|name|password|
|:--|:--|:--|:--|
|ダミーデータ１|"dummy_teacher"|"dummy_teacher"|"dummy_teacher"|

<br>

* school_classes

|カラム名||id|title|key|teacher_id|cook_id|
|:--|:--|:--|:--|:--|:--|
|ダミーデータ１|"dummy_school_class"|"dummy_school_class"|"dummy_teacher"|

<br>

* cooks  

|カラム名||id|name|teacher_id|user_id|created_at|user_grade|
|:--|:--|:--|:--|:--|:--|:--|
|ダミーデータ１|"dummy_cook"|"dummy_teacher"|null|作成時の時刻|t|

