# クラス図第12版(2023/02/03作成)

## 改版履歴
|版|作成者|作成日|概要|
|:--|:--|:--|:--|
|1版|全員|2022/12/2|クラス図の第一回を作成|
|2版|全員|2022/12/2|クラスの名前を変更、関連を修正|
|3版|鈴木・吉田・小島|2022/12/4|インスペクションを受け改善|
|4版|吉田|2022/12/4|23:51までのインスペクションを受けmdのみ改善、puファイルは未変更|
|5版|吉田・鈴木|2022/12/5|インスペクションを受け改善|
|6版|吉田・鈴木|2022/12/6|クラスの効率化|
|7版|吉田|2022/12/06|クラスの効率化|
|8版|鈴木・小島|2022/12/08|命名規則の変更|
|9版|小島・小林・塚越|2022/12/11|登録ステータスの追加|
|10版|塚越|2022/12/13|科目削除に関するステータスの追加|
|11版|塚越|2023/01/21|学生の科目履修に関するステータスの追加|
|12版|小島|2023/02/03|提出物の種類からお知らせを削除|



## 改版履歴詳細
|版|作成者|作成日|概要|
|:--|:--|:--|:--|
|2版|全員|2022/12/2|クラスの名前を変更、関連を修正|　

・命名規則の変更
・関連について修正

|版|作成者|作成日|概要|
|:--|:--|:--|:--|
|3版|鈴木・吉田・小島|2022/12/4|インスペクションを受け改善|

・命名規則の変更  
・enum型を追加  
・関連に関しての見直し  
・クラスの修正  

|版|作成者|作成日|概要|
|:--|:--|:--|:--|
|4版|吉田|2022/12/4|インスペクションを受け改善|

・クラスの追加  
・クラスの修正  

|版|作成者|作成日|概要|
|:--|:--|:--|:--|
|5版|吉田・鈴木|2022/12/5|インスペクションを受け改善|

・クラスの追加及び修正  
・属性について、createDateを各提出物に追加  

|版|作成者|作成日|概要|
|:--|:--|:--|:--|
|6版|吉田・鈴木|2022/12/5|クラスの効率化|

・levelCountを削除  
・gradeCountに役割を追加  


|版|作成者|作成日|概要|
|:--|:--|:--|:--|
|7版|吉田|2022/12/6|クラスの効率化|

・SubmissionDeadlineクラス追加に伴いDurationクラスの削除  
・NoticeクラスsubmissionType属性のenumを追加  


|版|作成者|作成日|概要|
|:--|:--|:--|:--|
|8版|鈴木・小島|2022/12/8|命名規則の変更|

・命名規則及び属性の一部の型を変更しました。

|版|作成者|作成日|概要|
|:--|:--|:--|:--|
|9版|小島・小林・塚越|2022/12/11|登録ステータスの追加|

・FieldResearchクラスとBasicSkillsクラスにsubmissionStatusの追加。

|版|作成者|作成日|概要|
|:--|:--|:--|:--|
|10版|塚越|2022/12/13|科目削除に関するステータスの追加|

・SubjectクラスにisDeleteの追加。

|版|作成者|作成日|概要|
|:--|:--|:--|:--|
|11版|塚越|2023/01/21|学生の科目履修に関するステータスの追加|

・SubjectUserRelationクラスにnoの追加。

|版|作成者|作成日|概要|
|:--|:--|:--|:--|
|12版|小島|2023/02/03|提出物の種類からお知らせを削除|

・Noticeクラス submissionTypeから「お知らせ」を削除

## ファイルの説明  
![class_11](class_11.png)
- クラス図の写真です。  

## クラスの説明  
### User
## ユーザーに対するクラス
|フィールド名|和名|型|その他|
|:--|:--|:--|:--:|
|id|ユーザーID|String|
|password|ログインパスワード|String|
|role|役割|Integer|
|name|名前|String|
|isLoginable|ログイン可能判断|Boolean|

### Student
## 学生に対するクラス
|フィールド名|和名|型|その他|
|:--|:--|:--|:--:|
|studentId|ユーザーID|String|Userクラスのid|
|teacherId|担当教員ID|String|Userクラスのid|
|grade|学年|Integer|
|belong|所属|Enum|次世代日本型教育システム研究開発専攻,教育支援協働実践開発専攻：教育AI研究プログラム,教育支援協働実践開発専攻：臨床心理学プログラム,教育支援協働実践開発専攻：教育協働研究プログラム|


### MasterThesis
## 修士論文または課題研究に対するクラス
|フィールド名|和名|型|その他|
|:--|:--|:--|:--:|
|studentId|学生ID|String|Userクラスのid|
|createDate|登録した日付|Date|
|masterMaintitle|主論文タイトル|String|
|masterSubtitle|副論文タイトル|String|
|subjectResearchtitle|課題研究タイトル|String|
|submissionStatus|登録ステータス|Enum|未登録,確認中,差し戻し中,登録済み|

### FieldResearch
## フィールド研究に対するクラス
|フィールド名|和名|型|その他|
|:--|:--|:--|:--:|
|studentId|学生ID|String|Userクラスのid|
|gradeCount|実施学年|Integer||
|createDate|登録した日付|Date|
|submissionStatus|登録ステータス|Enum|未登録,確認中,差し戻し中,登録済み(ただしここでは未登録,登録済みのいずれかの値しか取らない)|
|period|期間|String|
|subjectTitle|科目名|String|
|organizationName|外部組織名称|String|
|organizationNameh|外部組織名称フリガナ|String|
|organizationPostcode|外部組織郵便番号|String|
|organizationLocation|外部組織所在地|String|
|organizationPersosn|外部組織担当者|String|
|organizationPersonh|外部組織担当者フリガナ|String|
|organizationPhone|外部組織電話番号|String|
|organizationMail|外部組織メールアドレス|String|
|organizationEmergency|外部組織緊急連絡先|String|

### ResearchPlan 
## 研究計画に対するクラス
|フィールド名|和名|型|その他|
|:--|:--|:--|:--:|
|studentId|学生ID|String|Userクラスのid|
|createDate|登録した日付|Date|
|submissionStatus|登録ステータス|Enum|未登録,確認中,差し戻し中,登録済み|
|theme|テーマ|String|
|researchPurpose|研究目的及び研究計画書|String|
|isJudgementable|課題研究or修士論文|Boolean|
|findings|所見|String|
|gradeCount|学年|Integer|


### StudyPlan
## 修学計画に対するクラス
|フィールド名|和名|型|その他|
|:--|:--|:--|:--:|
|studentId|学生ID|String|Userクラスのid|
|submissionStatus|登録ステータス|Enum|未登録,確認中,差し戻し中,登録済み|
|findings|所見|String|
|gradeCount|学年|Integer|
|createDate|登録した日付|Date|

### SubjectUserRelation
## 学生が何の科目を履修しているかに対するクラス
|フィールド名|和名|型|その他|
|:--|:--|:--|:--:|
|no|識別ナンバー|Integer||
|studentId|学生ID|String|Userクラスのid|
|subjectId|科目ID|Integer|Subjectクラスのsubjectid|
|planGrade|履修予定学年・学期|Enum|1春,1秋,2春,2秋|

### Subject
## 科目に対するクラス
|フィールド名|和名|型|その他|
|:--|:--|:--|:--:|
|teacherId|教員ID|String|Userクラスのid|
|subjectId|科目ID|Integer|Subjectクラスのsubjectid|
|division|科目区分|Enum|専攻基盤科目,専攻基礎科目,専攻展開科目,専攻発展科目,特別研究,自専攻（自プログラム）以外の科目|
|unit|単位数|Integer|
|subjectName|科目名|String|
|semester|開講学期|Enum|1年春,1年秋,2年春,2年秋|
|isDelete|科目削除判断|Boolean|

### BasicSkills
## 社会人基礎スキルに対するクラス
|フィールド名|和名|型|その他|
|:--|:--|:--|:--:|
|studentId|学生ID|String|Userクラスのid|
|submissionStatus|登録ステータス|Enum|未登録,確認中,差し戻し中,登録済み(ただしここでは未登録,確認中,登録済みのいずれかの値しか取らない)|
|expertise|専門力|Enum|S,A,B,C|
|proposal|企画提案力|Enum|S,A,B,C|
|analytical|分析的実践力|Enum|S,A,B,C|
|communication|コミュニケーション力・チーム構成力|Enum|S,A,B,C|
|challenge|チャレンジ精神・主体性|Enum|S,A,B,C|
|findings|所見|String|
|lookBack|振り返り|String|
|gradeCount|学年|Integer|0:入学時,1:一年次,2:修了時|
|createDate|登録した日付|Date|


### Notice
## お知らせに対するクラス
|フィールド名|和名|型|その他|
|:--|:--|:--|:--:|
|senderId|差出人|String|Userクラスのid|
|noticeId|お知らせID|Integer|
|title|タイトル|String|
|text|本文|String|
|submissionType|提出物の種類|Enum|1年次修学計画書,2年次修学計画書,1年次研究計画書,2年次研究計画書,入学時社会人基礎スキル,1年次終了時社会人基礎スキル,修了時社会人基礎スキル,修士論文学位申請,フィールド研究A,フィールド研究B|
|start|表示期間開始日|Date||
|end|表示期間終了日|Date||



### Destination
## お知らせの宛先に対するクラス
|フィールド名|和名|型|その他|
|:--|:--|:--|:--:|
|noticeId|お知らせID|Integer|Noticeクラスのnoticeid|
|toUserId|宛先人|String|Userクラスのid|


### SubmissionDeadline
## 提出物の締切に対するクラス
|フィールド名|和名|型|その他|
|:--|:--|:--|:--:|
|submissionType|提出物の種類|Enum|1年次修学計画書,2年次修学計画書,1年次研究計画書,2年次研究計画書,入学時社会人基礎スキル,1年次終了時社会人基礎スキル,修了時社会人基礎スキル,修士論文学位申請,フィールド研究A,フィールド研究B|
|gradeCount|学年|Integer||
|start|表示期間開始日|Date||
|end|提出締切日|Date||



## 2.画面シナリオURL  
https://www.figma.com/file/FkWkjimmkPJ90uacywH7hq/Screen-Scenario?node-id=0%3A1&t=wQmyV8SttNmQyGCf-0
　
    
## 3.機能仕様書URL  
https://github.com/HazeyamaLab/SE22G1/blob/master/docs/function_specification.md
