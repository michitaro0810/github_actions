# データベース設計書

## 改版履歴
|版|作成者|作成日|概要|
|:--|:--|:--|:--|
|1版|@suzukisaya @e215405y @akari_hello @mgn901|2023/12/12|初版作成|


## 改版履歴詳細
|版|作成者|作成日|概要|
|:--|:--|:--|:--|
|1版|@suzukisaya @e215405y @akari_hello @mgn901|2023/12/12|初版作成|

##  テーブルの説明

### users

|フィールド名|和名|型|主キー|NULL|その他|
|:--|:--|:--|:--|:--|:--|
|id|ID|VARCHAR(16)|○|NO||
|user_mail|ユーザメールアドレス|VARCHAR(255)||NO||
|user_password_hash|ユーザパスワード|VARCHAR(64)||NO||

### employees

|フィールド名|和名|型|主キー|NULL|その他|
|:--|:--|:--|:--|:--|:--|
|id|ID|VARCHAR(16)|○|NO|usersテーブルのid|

### members

|フィールド名|和名|型|主キー|NULL|その他|
|:--|:--|:--|:--|:--|:--|
|id|ID|VARCHAR(16)|○|NO|usersテーブルのid|
|member_first_name|会員の姓|VARCHAR(30)||NO||
|member_first_name_kana|会員の姓のカタカナ表記|VARCHAR(30)||NO||
|member_last_name|会員の名|VARCHAR(30)||NO||
|member_last_name_kana|会員の名のカタカナ表記|VARCHAR(30)||NO||
|member_born_on|会員の誕生日|DATE||NO||
|member_sex|会員の性別|VARCHAR(64)||NO|sex_typesテーブルのname|
|member_telephone|会員の電話番号|VARCHAR(11)||NO||
|miles|所持マイル|INT||NO||

### tickets

|フィールド名|和名|型|主キー|NULL|その他|
|:--|:--|:--|:--|:--|:--|
|ticket_number|チケット番号|VARCHAR(10)|○|NO||
|member_id|ID|VARCHAR(16)||NULL|membersテーブルのid|
|is_head_ticket|そのチケットが座席予約の操作を行った会員本人のものであるか|TINYINT(1)||NO||
|passenger_first_name|座席を予約した会員または追加搭乗者の姓|VARCHAR(30)||NO||
|passenger_last_name|座席を予約した会員または追加搭乗者の名|VARCHAR(30)||NO||
|passenger_first_name_kana|座席を予約した会員または追加搭乗者の姓のカタカナ表記|VARCHAR(30)||NO||
|passenger_last_name_kana|座席を予約した会員または追加搭乗者の名のカタカナ表記|VARCHAR(30)||NO||
|passenger_born_on|座席を予約した会員または追加搭乗者の生年月日|DATE||NO||
|passenger_sex|座席を予約した会員または追加搭乗者の性別|VARCHAR(64)||NO|sex_typesテーブルのname|
|infant_first_name|座席を予約した会員または追加搭乗者の同伴者（幼児）の姓|VARCHAR(30)||NULL||
|infant_last_name|座席を予約した会員または追加搭乗者の同伴者（幼児）の名|VARCHAR(30)||NULL||
|infant_first_name_kana|座席を予約した会員または追加搭乗者の同伴者（幼児）の姓のカタカナ表記|VARCHAR(30)||NULL||
|infant_last_name_kana|座席を予約した会員または追加搭乗者の同伴者（幼児）の名のカタカナ表記|VARCHAR(30)||NULL||
|infant_born_on|座席を予約した会員または追加搭乗者の同伴者（幼児）の生年月日|DATE||NULL||
|infant_sex|座席を予約した会員または追加搭乗者の同伴者（幼児）の性別|VARCHAR(64)||NULL|sex_typesテーブルのname|
|is_boarding_procedure_completed|搭乗手続きが終了されたかどうか|TINYINT(1)||NO||
|transaction_id|取引ID|VARCHAR(16)||NO|transactionsテーブルのid|
|seat_number|座席番号|VARCHAR(255)|○|NO|seatsテーブルのseat_number|
|flight_number|便番号|VARCHAR(6)|○|NO|flightsテーブルのflight_number|
|flight_departured_on|出発日|DATE|○|NO|flightsテーブルのdepartured_on|

### transactions

|フィールド名|和名|型|主キー|NULL|その他|
|:--|:--|:--|:--|:--|:--|
|id|取引ID|VARCHAR(16)|○|NO||
|created_at|取引日時|DATETIME||NO|取引の行われた日時|
|authorization_id|決済番号|VARCHAR(16)||NULL|クレジットカード決済の決済番号|
|is_using_miles|マイル使用有無|TINYINT(1)||NO|マイルを使用して決済しているかどうか|
|member_id|会員ID|VARCHAR(16)||NO|membersテーブルのid|

### flights

|フィールド名|和名|型|主キー|NULL|その他|
|:--|:--|:--|:--|:--|:--|
|flight_number|便番号|VARCHAR(6)|○|NO|大文字の英字及び数字から成る文字列。1字以上6字以下。
|departured_on|出発日|DATE|○|NO|departured_atとは異なり、時刻の情報は持たないものとする
|departured_at|出発日時|DATETIME||NO|
|arrived_at|到着日時|DATETIME||NO|
|adult_firstclass_fee|ファーストクラス大人料金|INT||NO|
|adult_businessclass_fee|ビジネスクラス大人の料金|INT||NO|
|adult_economyclass_fee|エコノミークラス大人の料金|INT||NO|
|child_firstclass_fee|ファーストクラス小児の料金|INT||NO|
|child_businessclass_fee|ビジネスクラス小児の料金|INT||NO|
|child_economyclass_fee|エコノミークラス小児の料金|INT||NO|
|boarding_procedure_progress|搭乗手続きの状況|VARCHAR(64)||NO|boarding_procedure_progress_typesテーブルのname|
|departure_airport_id|到着地のID|VARCHAR(4)||NO|airportsテーブルのcode_in_4_letters|
|arrival_airport_id|到着地のID|VARCHAR(4)||NO|airportsテーブルのcode_in_4_letters|
|plane_model|航空機の型式|VARCHAR(255)||NO|planesテーブルのmodel|

### planes

|フィールド名|和名|型|主キー|NULL|その他|
|:--|:--|:--|:--|:--|:--|
|model|航空機の型式|VARCHAR(255)|○|NO|

### seats

|フィールド名|和名|型|主キー|NULL|その他|
|:--|:--|:--|:--|:--|:--|
|seat_number|座席番号|VARCHAR(255)|○|NO|航空機の座席番号。数字（1以上の整数。先頭が0であってはならない）と英字（大文字。1字）で表す。（例: 1A、20Fなど）。紐づけられている航空機の型式と組み合わせると一意になる。
|grade|座席クラス|VARCHAR(64)||NO|seat_grade_typesのname|
|plane_model|航空機の型式|VARCHAR(255)|○|NO|planesテーブルのmodel|

### base_mile_of_section

|フィールド名|和名|型|主キー|NULL|その他|
|:--|:--|:--|:--|:--|:--|
|base_miles|基本マイル|INT||NO||
|airport1_code_in_4letters|区間の始まり（または終わり）の空港の4レターコード|VARCHAR(4)|○|NO|airportsテーブルのcode_in_4letters|
|airport2_code_in_4letters|区間の終わり（または始まり）の空港の4レターコード|VARCHAR(4)|○|NO|airportsテーブルのcode_in_4letters|

### airports

|フィールド名|和名|型|主キー|NULL|その他|
|:--|:--|:--|:--|:--|:--|
|code_in_4_letters|4レターコード（ICAO空港コード）|VARCHAR(4)|○|NO||
|code_in_3_letters|3レターコード（IATA空港コード）|VARCHAR(3)||NO||
|name_in_japanese|空港名|VARCHAR(10)||NO||

### mile_coefficients_of_grade

|フィールド名|和名|型|主キー|NULL|その他|
|:--|:--|:--|:--|:--|:--|
|grade|座席クラス|VARCHAR(64)|○|NO|seat_grade_typesテーブルのname|
|coefficient|マイルの係数|FLOAT||NO||

### sex_types

|フィールド名|和名|型|主キー|NULL|その他|
|:--|:--|:--|:--|:--|:--|
|name|列挙子の名前|varchar(64)|○|NO|このテーブルには、このフィールドが`MALE`、`FEMALE`になっている2レコードのみが存在する。このフィールドを参照する他テーブルのフィールドの値は左記2つのみに制限される。|

### seat_grade_types

|フィールド名|和名|型|主キー|NULL|その他|
|:--|:--|:--|:--|:--|:--|
|name|列挙子の名前|varchar(64)|○|NO|このテーブルには、このフィールドが`FIRST_CLASS`、`BUSINESS_CLASS`、`ECONOMY_CLASS`になっている3レコードのみが存在する。このフィールドを参照する他テーブルのフィールドの値は左記3つのみに制限される。|

### boarding_procedure_progress_types

|フィールド名|和名|型|主キー|NULL|その他|
|:--|:--|:--|:--|:--|:--|
|name|列挙子の名前|varchar(64)|○|NO|このテーブルには、このフィールドが`NOT_STARTED`、`IN_PROGRESS`、`CLOSED`になっている3レコードのみが存在する。このフィールドを参照する他テーブルのフィールドの値は左記3つのみに制限される。|
