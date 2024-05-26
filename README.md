python -m venv scrapy-projects

<!-- source bin/activate -->

source Scripts/activate

pip install -r requirements.txt
<!--  -->

scrapy startproject topcv
cd topcv
touch topcv.json
scrapy genspider topcv-crawler https://www.topcv.vn/tim-viec-lam-moi-nhat

