# クラス図

## 改版履歴
|日付|版数|内容|
|:-:|:-:|:-:|
|2020/12/7|初版|
|2020/12/11|第2版|クラス図第1回インスペクションを受けての修正|
|2020/12/14|第3版|クラス図第2回インスペクションを受けての修正|




## ユーザに関するクラス
|クラス名|クラスの役割|備考|
|---|---|---|
|Student|生徒に関する情報をもつ||
|Teacher|教員に関する情報をもつ||

## 学校に関するクラス
|クラス名|クラスの役割|備考|
|---|---|---|
|School|学校に関する情報をもつ||

## チームに関するクラス
|クラス名|クラスの役割|備考|
|---|---|---|
|Team|チームに関する情報をもつ||
|TeamStudent|StudentとTeamの関連に関する情報をもつ||

## 献立に関するクラス
|クラス名|クラスの役割|備考|
|---|---|---|
|Plan|1日の献立に関する情報をもつ||
|Plan_team|献立とチームの関連に関する情報をもつ||
|Scene|1日の中での献立の状況に関する情報をもつ|※1|
|SceneMenu|SceneとMenuの関連に関する情報をもつ||
|Category|主食、副菜などのカテゴリー情報をもつ|例![例](https://user-images.githubusercontent.com/63034711/100466525-634c8c00-3114-11eb-933d-bdabe312de61.png)|
|Menu|食品に関する情報をもつ|例![例](https://user-images.githubusercontent.com/63034711/100466440-457f2700-3114-11eb-8004-6fa97bb41538.png)|
|MenuIngredient|MenuとIngredientの間の関連に関する情報をもつ||
|Ingredient|食材に含まれる食品及び食品の栄養素に関する情報をもつ|例![例](https://user-images.githubusercontent.com/63034711/100467461-d0acec80-3115-11eb-918e-1da092009fbd.png)|


※1 Sceneクラスのid,nameは以下の通り
|id|name|
|---|---|
|1|朝食|
|2|昼食|
|3|間食|
|4|夕食|