#环境基准地址
BASE_URL="http://192.168.10.131:8888/api/private/v1"
#excel测试用例地址
EXCEL_FILE="./data/测试用例.xlsx"
SHEET_NAME="Sheet1"
#mysql配置
DB_HOST="192.168.10.131"
DB_PORT=3306
DB_NAME="mydb"
DB_USER="root"
DB_PASSWORD="123456"
#sql资源销毁
SQL1='delete from sp_categoty where cat_name="大码服装"'
SQL2='delete from sp_categoty where attr_name="VIP尺码"'