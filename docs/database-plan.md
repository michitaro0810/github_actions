# DB設計書

## 改版履歴
|日付|担当者|変更内容|
|:-:|:-:|:-:|
|2020/11/27|美濃谷|たたき台作成|
|2020/12/07|池田|クラス図第1回インスペクションを基にした，たたき台の修正|
|2020/12/07|美濃谷|たたき台の修正，student,teacher,sceneテーブルに項目追加|
|2020/12/09|池田|team,category,menu_ingredientテーブルに項目追加|
|2020/12/11|近藤|ingredientsテーブルに項目追加，すべてのテーブル名を複数形に修正|
|2020/12/11|佐藤|schools,team_students,plans,scene_menus,menusに項目追加|
|2020/12/11|佐藤|string→varcharに修正，team_idをint型に修正，細かい言い回しの修正|
|2020/12/11|近藤|gradeをint型に修正，すべてのデータ型をMySQL同様大文字に修正|
|2020/12/15|佐藤|各テーブルのidの表記を，"テーブル名単数形_id"に修正，外部キーとして機能している場合は"テーブル名の短縮2文字_参照先のテーブル名単数形_id"に修正|
|2020/12/15|池田|誤字の修正|
|2020/12/18|美濃谷|○○_idや○○_nameをid,nameに変更,gradeのint型整数が表すものすべて列挙|
|2020/12/18|美濃谷|PKを全て〇で統一,DBインスペクションに基づく修正|
|2020/12/19|美濃谷|AUTO_INCREMENTのDEFAULT値削除|
|2021/1/22|美濃谷|plansテーブルのteam_idの外部キー制約を削除|

## ユーザに関するテーブル

### students
(生徒)
|カラム名|項目名|概要|データ型|NULLを許容|PK|DEFAULT|備考|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|id|生徒ID|VARCHAR(16)|NO|〇|NULL||
|password|パスワード|VARCHAR(255)|NO||NULL|暗号化検討|
|name|生徒名|VARCHAR(15)|NO||NULL||
|sex|性別|INT|NO||0||
|school_id|学校ID|INT|NO||NULL||
|grade|学年|INT|NO||NULL||
|classnumber|組|VARCHAR(5)|NO||NULL||
|number|番号|VARCHAR(5)|NO||NULL||
|created_at|作成日時|DATETIME|NO||NULL|current_date|
|updated_at|更新日時|DATETIME|NO||NULL|current_date|

### teachers
(教員)
|カラム名|項目名|概要|データ型|NULLを許容|PK|DEFAULT|備考|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|id|教員ID|VARCHAR(16)|NO|〇|NULL||
|name|教員名|VARCHAR(15)|NO||NULL||
|password|パスワード|VARCHAR(255)|NO||NULL|暗号化検討|
|school_id|学校ID|INT|NO||NULL||
|created_at|作成日時|DATETIME|NO||NULL|current_date|
|updated_at|更新日時|DATETIME|NO||NULL|current_date|

## 学校に関するテーブル

### schools
(学校)
|カラム名|項目名|概要|データ型|NULLを許容|PK|DEFAULT|備考|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|id|学校id|INT|NO|〇||AUTO_INCREMENT|
|name|学校名|VARCHAR(30)|NO||NULL|UNIQUE|

## チームに関するテーブル

### team_students
(中間テーブル)
|カラム名|項目名|概要|データ型|NULLを許容|PK|DEFAULT|備考|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|team_id|チームID|INT|NO||0|外部キー(team.id)|
|user_id|ユーザID|INT|NO||0|外部キー(user.id)|

### teams
(チーム)
|カラム名|項目名|概要|データ型|NULLを許容|PK|DEFAULT|備考|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|id|ID|INT|NO|〇||auto_increment|
|name|チーム名|VARCHAR(100)|NO||NULL||
|teachar_id|教員ID|VARCHAR(16)|NO||NULL|外部キー(参照先:teacharテーブルのteachar_id)|

## 献立に関するテーブル

### plans
(献立)
|カラム名|項目名|概要|データ型|NULLを許容|PK|DEFAULT|備考|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|id|献立id|INT|NO|〇||AUTO_INCREMENT|
|name|献立名|VARCHAR(50)|YES||NULL||
|user_id|作成者id|YES||NULL|外部キー(students.id)|
|team_id|献立チームid|INT|YES||NULL||
|grade|作成時学年|INT|NO||NULL|外部キー(students.grade)|
|created_at|作成日|DATE|NO||NULL||

### scenes
(朝食などの食事)
|カラム名|項目名|概要|データ型|NULLを許容|PK|DEFAULT|備考|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|id|ID|INT|NO|〇||auto_increment|
|name|食事名|VARCHAR(3)|NO||NULL||
|plan_id|プランID|INT|NO||NULL|外部キー(plans.id)|
|created_at|作成日時|DATETIME|NO||NULL|current_date|
|updated_at|更新日時|DATETIME|NO||NULL|current_date|

### scene_menus
(中間テーブル)
|カラム名|項目名|概要|データ型|NULLを許容|PK|DEFAULT|備考|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|id|ID|INT|NO|〇||AUTO_INCREMENT|
|quantity|量|FLOAT|NO||0||
|scene_id|ユーザID|INT|NO||1|外部キー(scenes.id)|
|menu_id|ユーザID|INT|NO||0|外部キー(menus.id)|

### categories
(カテゴリ)
|カラム名|項目名|概要|データ型|NULLを許容|PK|DEFAULT|備考|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|id|ID|カテゴリを一意に識別するための番号|INT|NO|〇||auto_increment|
|name|カテゴリ名|カテゴリの名前（主食，主菜，副菜，汁物，デザート）|VARCHAR(8)|NO||NULL||
|created_at|作成日時|DATETIME|NO||NULL|current_date|
|updated_at|更新日時|datetime|NO||NULL|current_date|

### menus
(食品)
|カラム名|項目名|概要|データ型|NULLを許容|PK|DEFAULT値|備考|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|id|ID|INT|NO|〇||AUTO_INCREMENT|
|name|食品名|VARCHAR(255)|YES||NULL||
|category_id|カテゴリID|INT|NO||99|外部キー(categories.id)|

### menu_ingredients
(中間テーブル)
|カラム名|項目名|概要|データ型|NULLを許容|PK|DEFAULT|備考|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|id|ID|INT|NO|〇||auto_increment|
|quantity|食事量|FLOAT|NO||0||
|menu_id|メニューID|INT|NO||0|外部キー(参照先:menuテーブルのmenu_id)|
|ingredient_id|材料ID|INT|NO||0|外部キー(参照先:ingredientテーブルのingredients_id)|
|created_at|作成日時|DATETIME|NO||NULL|current_date|
|updated_at|更新日時|DATETIME|NO||NULL|current_date|

### ingredients
(食品に含まれる材料)
|カラム名|項目名|概要|データ型|NULLを許容|PK|DEFAULT|備考|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|id|ID|INT|NO|〇||auto_increment|
|group_id|食品群番号||INT|NO||NULL||
|name|食品に含まれる材料名||VARCHAR(255)|NO||NULL||
|base_quantity|分量(g)||INT|NO||NULL||
|points|分量当たりの点数||FLOAT|NO||NULL||
|disposal_rate|廃棄率||INT|NO||NULL||
|energy|エネルギー||INT|NO||NULL||
|water|水分||FLOAT|NO||NULL||
|protein|タンパク質||FLOAT|NO||NULL||
|total_fat|脂質||FLOAT|NO||NULL||
|saturated_fat|飽和脂肪酸||FLOAT|NO||NULL||
|monounsaturated_fatty_acid|一価不飽和脂肪酸||FLOAT|NO||NULL||
|polyunsaturated_fatty_acid|多価不飽和脂肪酸||FLOAT|NO||NULL||
|cholesterol|コレステロール||FLOAT|NO||NULL||
|total_carbohydrate|炭水化物||FLOAT|NO||NULL||
|water_soluble _dietary_fiber|水溶性食物繊維||FLOAT|NO||NULL||
|insoluble_dietary_fiber|不溶性食物繊維||FLOAT|NO||NULL||
|total_dietary_fiber|食物繊維総量||FLOAT|NO||NULL||
|ash|灰分||FLOAT|NO||NULL||
|sodium|ナトリウム||FLOAT|NO||NULL||
|potassium|カリウム||FLOAT|NO||NULL||
|calcium|カルシウム||FLOAT|NO||NULL||
|magnesium|マグネシウム||FLOAT|NO||NULL||
|rin|リン||FLOAT|NO||NULL||
|iron|鉄||FLOAT|NO||NULL||
|zinc|亜鉛||FLOAT|NO||NULL||
|copper|銅||FLOAT|NO||NULL||
|manganese|マンガン||FLOAT|NO||NULL||
|lodine|ヨウ素||FLOAT|NO||NULL||
|selenium|セレン||FLOAT|NO||NULL||
|chromium|クロム||FLOAT|NO||NULL||
|molybdenum|リブデン||FLOAT|NO||NULL||
|retinol_activity_equivalents|レチノール活性当量||FLOAT|NO||NULL||
|vitamin_d|ビタミンD||FLOAT|NO||NULL||
|alpha-tocopherol|α-トコフェロール||FLOAT|NO||NULL||
|vitamin_k|ビタミンK||FLOAT|NO||NULL||
|vitamin_b1|ビタミンB1||FLOAT|NO||NULL||
|vitamin_b2|ビタミンB2||FLOAT|NO||NULL||
|niacin|ナイアシン||FLOAT|NO||NULL||
|niacin_equivalent|ナイアシン当量||FLOAT|NO||NULL||
|vitamin_b6|ビタミンB6||FLOAT|NO||NULL||
|vitamin_b12|ビタミンB12||FLOAT|NO||NULL||
|folate|葉酸||FLOAT|NO||NULL||
|pantothenic_acid|パントテン酸||FLOAT|NO||NULL||
|biotin|ビオチン||FLOAT|NO||NULL||
|vitamin_c|ビタミンC||FLOAT|NO||NULL||
|salt_equivalents|食塩相当量||FLOAT|NO||NULL||
|starch|でんぷん||FLOAT|NO||NULL||
|glucose|ぶどう糖||FLOAT|NO||NULL||
|fructose|果糖||FLOAT|NO||NULL||
|galactose|ガラクトース||FLOAT|NO||NULL||
|sucrose|しょ糖||FLOAT|NO||NULL||
|maltose|麦芽糖||FLOAT|NO||NULL||
|lactose|乳糖||FLOAT|NO||NULL||
|trehalose|トレハロース||FLOAT|NO||NULL||
|sorbitol|ソルビトール||FLOAT|NO||NULL||
|mannitol|マンニトール||FLOAT|NO||NULL||
|quantity_of_fatty_acid|脂肪酸総量||FLOAT|NO||NULL||
|saturated_fatty_acid|飽和脂肪酸||FLOAT|NO||NULL||
|monounsaturated_fatty_acids|一価不飽和脂肪酸||FLOAT|NO||NULL||
|polyunsaturated_fatty_acids|多価不飽和脂肪酸||FLOAT|NO||NULL||
|n-3_polyunsaturated_fatty_acids|n-3系多価不飽和脂肪酸||FLOAT|NO||NULL||
|n-6_polyunsaturated_fatty_acids|n-6系多価不飽和脂肪酸||FLOAT|NO||NULL||
|butyric_acid(4:0)|酪酸（4:0）||FLOAT|NO||NULL||
|caproic_acid(6:0)|ヘキサン酸（6:0）||FLOAT|NO||NULL||
|enanthic_acid(7:0)|ヘプタン酸（7:0）||FLOAT|NO||NULL||
|octanoic_acid(8:0)|オクタン酸（8:0）||FLOAT|NO||NULL||
|decanoic_acid(10:0)|デカン酸（10:0）||FLOAT|NO||NULL||
|lauric_acid(12:0)|ラウリン酸（12:0）||FLOAT|NO||NULL||
|tridecanoic_acid(13:0)|トリデカン酸（13:0）||FLOAT|NO||NULL||
|myristic_acid(14:0)|ミリスチン酸（14:0）||FLOAT|NO||NULL||
|pentadecylic_acid(15:0)|ペンタデカン酸(15:0)||FLOAT|NO||NULL||
|pentadecylic_acid(15:0ant)|ペンタデカン酸(15:0 ant)||FLOAT|NO||NULL||
|palmitic_acid(16:0)|パルミチン酸(16:0)||FLOAT|NO||NULL||
|palmitic_acid(16:0iso)|パルミチン酸(16:0 iso)||FLOAT|NO||NULL||
|heptadecanic_acid(17:0)|ヘプタデカン酸(17:0)||FLOAT|NO||NULL||
|heptadecanic_acid(17:0ant)|ヘプタデカン酸(17:0 ant)||FLOAT|NO||NULL||
|stearic_acid(18:0)|ステアリン酸(18:0)||FLOAT|NO||NULL||
|arachidic_acid(20:0)|アラキジン酸(20:0)||FLOAT|NO||NULL||
|behenic_acid(20:0)|ベヘン酸(20:0)||FLOAT|NO||NULL||
|lignoceric_acid(24:0)|ノセリン酸(24::0)||FLOAT|NO||NULL||
|decenoic_acid(10:1)|デセン酸(10.1)||FLOAT|NO||NULL||
|myristoleic_acid(14:1)|ミリストレイン酸(14:1)||FLOAT|NO||NULL||
|pentadecenoic_acid(15:1)|ペンタデセン酸(15:1)||FLOAT|NO||NULL||
|palmitoleic_acid(16:1)|パルミトレイン酸(16:1)||FLOAT|NO||NULL||
|heptadecenoic_acid(17:1)|ヘプタデセン酸(17:1)||FLOAT|NO||NULL||
|n-9_oleic_acid(18: 1)|n-9オレイン酸(18:1)||FLOAT|NO||NULL||
|n-7_sith-vaccenic_acid(18:1)|n-7シス-バクセン酸(18:1)||FLOAT|NO||NULL||
|icosenoic_acid(20:1)|イコセン酸(20:1)||FLOAT|NO||NULL||
|docosenoic_acid(20:1)|ドコセン酸(22:1)||FLOAT|NO||NULL||
|tetracosane_acid(21:1)|テトラコセン酸(24:1)||FLOAT|NO||NULL||
|hexadecadienoic_acid(16:2)|ヘキサデカジエン酸||FLOAT|NO||NULL||
|hexadecatrienoic_acid(16:3)|ヘキサデカトリエン酸(16:3)||FLOAT|NO||NULL||
|hexadecatetraenoic_acid(16:4)|ヘキサデカテトラエン酸(16:4)||FLOAT|NO||NULL||
|heptadecadienoic_acid(17:2)|ヘプタデカジエン酸(17:2)||FLOAT|NO||NULL||
|heptadecadienoic_acid(18:2)|オクタデカジエン酸(18:2)||FLOAT|NO||NULL||
|n-6_linoleic_acid(18:2)|n-6リノール酸(18:2)||FLOAT|NO||NULL||
|octadecatrienoic_acid(18:3)|オクタデカトリエン酸(18:3)||FLOAT|NO||NULL||
|n-3_alpha-linolenic_acid(18:3)|n-3α‐リノレン酸(18:3)||FLOAT|NO||NULL||
|n-6_ gamma-linolenic_acid(18:3)|n-6γ‐リノレン酸(18:3)||FLOAT|NO||NULL||
|n-3_octadecatetraenoic_acid(18:4)|n-3オクタデカテトラエン酸(18:4)||FLOAT|NO||NULL||
|n-6_icosadienoic_acid(20:2)|n-6イコサジエン酸(20:2)||FLOAT|NO||NULL||
|n-6_Icosatrienoic_acid(20:3)|n-6イコサトリエン酸(20:3)||FLOAT|NO||NULL||
|n-3_eicosatetraenoic_acid(20:4)|n-3イコサテトラエン酸(20:4)||FLOAT|NO||NULL||
|n-6_arachidonic_acid(20:4)|n-6アラキドン酸(20:4)||FLOAT|NO||NULL||
|n-3_eicosapentaenoic_acid(20:5)|n-3イコサペンタエン酸(20:5)||FLOAT|NO||NULL||
|n-3_eicosapentaenoic_acid(21:5)|n-3ヘンイコサペンタエン酸(21:5)||FLOAT|NO||NULL||
|docosadienoic_acid(22:2)|ドコサジエン酸(22:2)||FLOAT|NO||NULL||
|n-6_docosatetraenoic_acid(22:4)|n-6ドコサテトラエン酸(22:4)||FLOAT|NO||NULL||
|n-3_docosapentaenoic_acid(22:5)|n-3ドコサペンタエン酸(22:5)||FLOAT|NO||NULL||
|n-6_docosapentaenoic_acid(22:5)|n-6ドコサペンタエン酸(22:5)||FLOAT|NO||NULL||
|n-3_docosahexaenoic_acid(22:6)|n-3ドコサヘキサエン酸(22:6)||FLOAT|NO||NULL||
|created_at|作成日時|DATETIME|NO|CURRENT_TIMESTAMP|DEFAULT_GENERATED|
|updated_at|更新日時|DATETIME|NO|CURRENT_TIMESTAMP|DEFAULT_GENERATED on update CURRENT_TIMESTAMP|
