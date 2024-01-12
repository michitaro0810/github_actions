### Teacher

|フィールド名|和名|型|その他|
|:--|:--|:--|:--|
|id||String||
|name||string||
|password||string||
|schoolId||int||

### Student

|フィールド名|和名|型|その他|
|:--|:--|:--|:--|
|id||string||
|password||string||
|name||string||
|sex||int||
|grade||int||
|classNumber||string||
|number||string||

### School

|フィールド名|和名|型|その他|
|:--|:--|:--|:--|
|id||int||
|name||string||

### TeamStudent

|フィールド名|和名|型|その他|
|:--|:--|:--|:--|
|teamId||int||
|userId||int||

### Plan

|フィールド名|和名|型|その他|
|:--|:--|:--|:--|
|id||int||
|name||string||
|grade||string||
|userId||int||
|teamId||int||

### Team

|フィールド名|和名|型|その他|
|:--|:--|:--|:--|
|id||int||
|name||string||
|teacherId||int||

### Scene

|フィールド名|和名|型|その他|
|:--|:--|:--|:--|
|id||int||
|name||string||
|planId||int||

### PlanTeam

|フィールド名|和名|型|その他|
|:--|:--|:--|:--|
|planId||int||
|teamId||int||

### Category

|フィールド名|和名|型|その他|
|:--|:--|:--|:--|
|id||int||
|name||string||

### SceneMenu

|フィールド名|和名|型|その他|
|:--|:--|:--|:--|
|id||int||
|quantity||float||
|sceneId||int||
|menuId||int||

### Menu

|フィールド名|和名|型|その他|
|:--|:--|:--|:--|
|id||int||
|name||string||
|categoryId||int||

### MenuIngredient

|フィールド名|和名|型|その他|
|:--|:--|:--|:--|
|id||int||
|quantity||float||
|menuId||int||
|ingredientsId||int||

### Ingredient

|フィールド名|和名|型|その他|
|:--|:--|:--|:--|
|id||int||
|groupId||int||
|name||string||
|baseQuantity||int||
|points||float||
|disposalRate||int||
|energy||int||
|water||float||
|protein||float||
|totalFat||float||
|saturatedFat||float||
|monounsaturatedFat||float||
|monounsaturatedFattyAcid||float||
|polyunsaturatedFattyAcid||float||
|cholesterol||float||
|totalCarbohydrate||float||
|waterSolubleDietaryFiber||float||
|insolubleDietaryFiber||float||
|totalDietaryFiberash||float||
|ash||float||
|sodium||float||
|potassium||float||
|calcium||float||
|magnesium||float||
|rin||float||
|iron||float||
|zinc||float||
|copper||float||
|manganese||float||
|lodine||float||
|selenium||float||
|chromium||float||
|molybdenum||float||
|retinolActivityEquivalents||float||
|vitaminD||float||
|alphaTocopherrol||float||
|vitaminK||float||
|vitaminB1||float||
|vitaminB2||float||
|niacin||float||
|niacinEquivalent||float||
|vitaminB6||float||
|vitaminB12||float||
|folate||float||
|pantothenicAcid||float||
|biotin||float||
|vitaminC||float||
|saltEquivalents||float||
|starch||float||
|glucose||float||
|fructose||float||
|galactose||float||
|sucrose||float||
|maltose||float||
|lactose||float||
|trehalose||float||
|sorbitol||float||
|mannitol||float||
|quantityOfFattyAcid||float||
|saturatedFattyAcid||float||
|monounsaturatedFattyAcids||float||
|polyunsaturatedFattyAcids||float||