# データベース図第11版(2023/02/03作成)

## 改版履歴
|版数|作成者|作成日|概要|
|:--:|:--|:--:|:-|
|1版|吉田|2022/11/21|全体の形を作成|
|2版|吉田・鈴木|2022/12/06|クラス図を受けて修正|
|3版|鈴木・吉田|2022/12/07|第一回インスペクションを受けて修正|
|4版|鈴木・小島|2022/12/08|命名規則の統一|
|5版|鈴木・小島|2022/12/08|その他の説明補充|
|6版|小島・小林・塚越|2022/12/11|登録ステータスの追加|
|7版|塚越|2022/12/13|科目削除に関するステータスの追加|
|8版|吉田|2023/01/18|subject_user_relationsに主キーを追加|
|9版|塚越|2023/01/20|usersテーブルのidにBINARY属性を追加|
|10版|小林|2023/01/27|型定義の修正|
|11版|小島|2023/02/03|提出物の種類からお知らせを削除|

****
## 改版履歴詳細
|版|作成者|作成日|概要|
|:--|:--|:--|:--|
|2版|吉田|2022/12/06|クラス図を受け手修正|

・新たなテーブルを追加  
・NOTNULL制約の活用を復活  

****

|版|作成者|作成日|概要|
|:--|:--|:--|:--|
|3版|鈴木・吉田|2022/12/07|第一回インスペクションを受けて修正|

・命名規則の変更  
・enum型をinteger型に変更  
・integer変更につき、添え字の付与
・passwordのアルゴリズムの記載  

****


|版|作成者|作成日|概要|
|:--|:--|:--|:--|
|4版|鈴木・小島|2022/12/08|命名規則修正|
 
・スネークケースに書き換える  
・date型の命名規則を統一


|版|作成者|作成日|概要|
|:--|:--|:--|:--|
|5版|鈴木・小島|2022/12/08|その他の説明補充|
 
・不足していたその他の項目の説明を記載。

|版|作成者|作成日|概要|
|:--|:--|:--|:--|
|6版|小島・小林・塚越|2022/12/11|登録ステータスの追加|
 
・FieldResearchクラスとBasicSkillsクラスにsubmissionStatusの追加。

|版|作成者|作成日|概要|
|:--|:--|:--|:--|
|7版|塚越|2022/12/13|科目削除に関するステータスの追加|
 
・subjectsテーブルにis_deleteの追加。

|版|作成者|作成日|概要|
|:--|:--|:--|:--|
|8版|吉田|2023/01/18|subject_user_relationsに主キーを追加|
 
・subject_user_relationsテーブルに主キー「no」を追加  
・subject_user_relations内の重複データを削除可能に変更

|版|作成者|作成日|概要|
|:--|:--|:--|:--|
|9版|塚越|2023/01/20|usersテーブルの修正|
 
・usersテーブルのidにBINARY属性を追加

|版|作成者|作成日|概要|
|:--|:--|:--|:--|
|10版|小林|2023/01/27|型定義の修正|
 
・created_at,research_purpose,findingsの型をvarcharに変更  
・is_judgementableの型をintegerに変更

|版|作成者|作成日|概要|
|:--|:--|:--|:--|
|11版|小島|2023/02/03|提出物の種類からお知らせを削除|
 
・noticesテーブル submission_type から「お知らせ」を削除


****

### users
|カラム名|和名|型|主キー|NULL|その他|
|:--|:--|:--|:--:|:--:|:--|
|id|ユーザーID|varchar(10)|○|NO|BINARY属性|
|password|ログインパスワード|varchar(64)||NO|SHA-2でハッシュ化|
|role|役割|integer||NO|1:学生,2:教員,3:職員|
|name|名前|varchar(30)||NO||
|is_loginable|ログイン可能判断|boolean||NO|TRUE:可能,FALSE:不可能|

### students
|カラム名|和名|型|主キー|NULL|その他|
|:--|:--|:--|:--:|:--:|:--|
|student_id|ユーザーID|varchar(10)|○|NO|外部キー:userテーブルのid|
|teacher_id|担当教員ID|varchar(10)||NO|外部キー:userテーブルのid|
|grade|学年|integer||NO|0の数字が入学時、1が1年次、2が2年次、3以上の数値が留年した人|
|belong|所属|integer||NO|1:次世代日本型教育システム研究開発専攻,2:教育支援協働実践開発専攻：教育AI研究プログラム,3:教育支援協働実践開発専攻：臨床心理学プログラム,4:教育支援協働実践開発専攻：教育協働研究プログラム|



### master_thesises
## 修士論文
|カラム名|和名|型|主キー|NULL|その他|
|:--|:--|:--|:--:|:--:|:--|
|student_id|学生ID|varchar(10)|○|NO|外部キー:userテーブルのid|
|created_at|登録した日付|varchar(40)||NO||
|master_main_title|主論文タイトル|varchar(100)||YES||
|master_sub_title|副論文タイトル|varchar(100)||YES||
|subject_research_title|課題研究タイトル|varchar(100)||YES||
|submission_status|登録ステータス|integer||NO|1:未登録,2:確認中,3:差し戻し中,4:登録済み|


### field_researches
## フィールド研究
|カラム名|和名|型|主キー|NULL|その他|
|:--|:--|:--|:--:|:--:|:--|
|student_id|学生ID|varchar(10)||NO|外部キー:userテーブルのid|
|grade_count|実施学年|integer||NO||
|submission_status|登録ステータス|integer||NO|1:未登録,2:確認中,3:差し戻し中,4:登録済み(ただしここでは1,4のいずれかの値しか取らない)|
|period|期間|varchar(23)||NO||
|subject_title|科目名|varchar(100)||NO||
|organization_name|外部組織名称|varchar(100)||NO||
|organization_nameh|外部組織名称フリガナ|varchar(100)||NO||
|organization_postcode|外部組織郵便番号|varchar(8)||NO||
|organization_location|外部組織所在地|varchar(100)||NO||
|organization_persosn|外部組織担当者|varchar(30)||NO||
|organization_personh|外部組織担当者フリガナ|varchar(100)||NO||
|organization_phone|外部組織電話番号|varchar(20)||NO||
|organization_mail|外部組織メールアドレス|varchar(100)||NO||
|organization_emergency|外部組織緊急連絡先|varchar(20)||NO||
|created_at|登録した日付|varchar(40)||NO||


### research_plans
## 研究計画書
|カラム名|和名|型|主キー|NULL|その他|
|:--|:--|:--|:--:|:--:|:--|
|student_id|学生ID|varchar(10)||NO|外部キー:userテーブルのid|
|created_at|登録した日付|varchar(40)||NO||
|submission_status|登録ステータス|integer||NO|1:未登録,2:確認中,3:差し戻し中,4:登録済み|
|theme|テーマ|varchar(100)||NO||
|research_purpose|研究目的及び研究計画|varchar(100)||NO||
|is_judgementable|課題研究or修士論文|integer||NO|課題研究：Trueで修士論文：False|
|findings|所見|varchar(100)||YES|教員による記入|
|grade_count|学年|integer||NO||


### study_plans
## 修学計画書
|カラム名|和名|型|主キー|NULL|その他|
|:--|:--|:--|:--:|:--:|:--|
|student_id|学生ID|varchar(10)||NO|外部キー:userテーブルのid|
|submission_status|登録ステータス|integer||NO|1:未登録,2:確認中,3:差し戻し中,4:登録済み|
|findings|所見|varchar(100)||YES|教員による記入|
|grade_count|学年|integer||NO||
|created_at|登録した日付|varchar(40)||NO||


### subject_user_relations
|カラム名|和名|型|主キー|NULL|その他|
|:--|:--|:--|:--:|:--:|:--|
|no|識別ナンバー|integer|○|NULL|オートインクリメント|
|student_id|学生ID|varchar(10)||NO|外部キー:userテーブルのid|
|subject_id|科目ID|integer||NO|外部キー:subjectテーブルのsubjectid|
|plan_grade|履修予定学年・学期|integer||NO|1:1春,2:1秋,3:2春,4:2秋|

### subjects
|カラム名|和名|型|主キー|NULL|その他|
|:--|:--|:--|:--:|:--:|:--|
|teacher_id|教員ID|varchar(10)||NO|外部キー:userテーブルのid|
|subject_id|科目ID|integer|○|NO|オートインクリメント|
|division|科目区分|integer||NO|1:専攻基盤科目,2:専攻基礎科目,3:専攻展開科目,4:専攻発展科目,5:特別研究,6:自専攻（自プログラム）以外の科目|
|unit|単位数|integer||NO||
|subject_name|科目名|varchar(50)||NO||
|semester|開講学期|integer||NO|1:1年春,2:1年秋,3:2年春,4:2年秋|
|is_delete|科目削除判断|boolean||NO|TRUE:削除,FALSE:未削除|

### basic_skills
|カラム名|和名|型|主キー|NULL|その他|
|:--|:--|:--|:--:|:--:|:--|
|student_id|学生ID|varchar(10)||NO|外部キー:userテーブルのid|
|submission_status|登録ステータス|integer||NO|1:未登録,2:確認中,3:差し戻し中,4:登録済み(ただしここでは1,2,4のいずれかの値しか取らない)|
|expertise|専門力|integer||NO|1:S,2:A,3:B,4:C|
|proposal_plan|企画提案力|integer||NO|1:S,2:A,3:B,4:C|
|analytical|分析的実践力|integer||NO|1:S,2:A,3:B,4:C|
|communication|コミュニケーション力・チーム構成力|integer||NO|1:S,2:A,3:B,4:C|
|challenge|チャレンジ精神・主体性|integer||NO|1:S,2:A,3:B,4:C|
|lookback|振り返り|text||YES||
|grade_count|学年|integer||NO|0:入学時,1:1年次,2:修了時|
|findings|所見|varchar(100)||YES|教員による記入|
|created_at|登録した日付|varchar(40)||NO||

### notices
|カラム名|和名|型|主キー|NULL|その他|
|:--|:--|:--|:--:|:--:|:--|
|sender_id|差出人|varchar(10)||NO|外部キー:userテーブルのid|
|notice_id|お知らせid|integer|○|NO|オートインクリメント|
|title|タイトル|varchar(50)||NO||
|text|本文|text||NO||
|submission_type|提出物の種類|integer||NO|1:1年次修学計画書,2:2年次修学計画書,3:1年次研究計画書,4:2年次研究計画書,5:入学時社会人基礎スキル,6:1年次終了時社会人基礎スキル,7:修了時社会人基礎スキル,8:修士論文学位申請,9:フィールド研究A,10:フィールド研究B|
|started_at|表示期間開始日|date||NO||
|ended_at|表示期間終了日|date||NO||


### destinations
|カラム名|和名|型|主キー|NULL|その他|
|:--|:--|:--|:--:|:--:|:--|
|notice_id|お知らせid|integer||NO|外部キー:noticeテーブルのnoticeid|
|to_user_id|宛先人|varchar(10)||NO|外部キー:userテーブルのid|


### submission_deadlines
|カラム名|和名|型|主キー|NULL|その他|
|:--|:--|:--|:--:|:--:|:--|
|submission_type|提出物の種類|integer||NO|1:1年次修学計画書,2:2年次修学計画書,3:1年次研究計画書,4:2年次研究計画書,5:入学時社会人基礎スキル,6:1年次終了時社会人基礎スキル,7:修了時社会人基礎スキル,8:修士論文学位申請,9:フィールド研究A,10:フィールド研究B|
|grade_count|学年|integer||NO||
|started_at|表示期間開始日|date||NO||
|ended_at|締切・表示期間終了日|date||NO||
