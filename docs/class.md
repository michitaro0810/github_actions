
## 改版履歴
|版|作成者|作成日|概要|
|:--|:--|:--|:--:|
|初版|進藤瑠里|2023/11/28|クラス図|
<br>

## 改版履歴詳細
|版|作成者|作成日|概要|
|:--|:--|:--|:--:|
|初版|進藤瑠里|2023/11/28|クラス図|
<br>

## クラス図の画像
![クラス図](./class_diagram.png)


## クラスの説明

### User
ユーザーに対するクラス
|フィールド名|和名|型|その他|
|:--|:--|:--|:--:|
|userName|ユーザー名|String|
|userBirthday|生年月日|String|
|userSex|性別|enum|
|userMailadress|メールアドレス|String|
|userPassword|パスワード|String|
|mileagePossess|保有マイル|int|
|flightAward|特典航空券|boolean|
<br>

### FlightAward
特典航空券に対するクラス
|フィールド名|和名|型|その他|
|:--|:--|:--|:--:| 
|flightId|フライトID|int|
|seatingGrade|座席のグレード|enum|
|seatingFare|座席の運賃|enum|
|numOfFlightAward|特典航空券の枚数|int|
<br>
    

### Regist
予約に対するクラス
|フィールド名|和名|型|その他|
|:--|:--|:--|:--:|
|registId|予約ID|int|
|flightId|フライトID|int|
|userMailadress|メールアドレス|String|
|registStatus|予約状況|enum|
|numOfAccompany|同行者人数|int|
|price|料金|int|
|paymentMethods|決済方法|String|
|earnMile|獲得マイル|int|
|userSeatNum|ユーザー座席番号|String|
<br>


### Flight
フライトに対するクラス
|フィールド名|和名|型|その他|
|:--|:--|:--|:--:|
|flightId|フライトID|int|
|aircraftType|機体名|String|
|depatureLocation|出発地|String|
|arrivalLocation|到着地|String|
|depaturetime|出発時刻|Date|
|arrivalTime|到着時刻|Date|
|Fare|運賃|int|
|seatCapacity|座席数|int|
|bordingGate|搭乗口|String|
|basicSectorMile|基本マイル|int|
<br>


#### Accompany
同行者に対するクラス
|フィールド名|和名|型|その他|
|:--|:--|:--|:--:|
|registId|予約ID|int|
|accompanyName|同行者名|String|
|accompanyBirthday|同行者の生年月日|Date|
|accompanySex|同行者の性別|enum|
|accompanySeatNum|同行者の座席番号|String|
<br>

### SeatingCapacity
座席数に対するクラス
|フィールド名|和名|型|その他|
|:--|:--|:--|:--:|
|premiumSeatingCapacity|プレミアムクラスの座席数|int|
|economySeatingCapacity|エコノミークラスの座席数|int|
<br>

### SeatingGrade
座席のグレードに対するクラス
|フィールド名|和名|型|その他|
|:--|:--|:--|:--:|
|premiumClass|プレミアムクラス|String|
|economyClass|エコノミークラス|String|
<br>

### SeatFare
運賃に対するクラス
|フィールド名|和名|型|その他|
|:--|:--|:--|:--:|
|adultPremiumFare|大人料金（プレミアムクラス）|int|
|adultEconomyFare|大人料金（エコノミークラス）|int|
|childPremiumFare|子供料金（プレミアムクラス）|int|
|childEconomyFare|子供料金（エコノミークラス）|int|
<br>





