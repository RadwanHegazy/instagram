apt-get update
apt-get install -y imagemagick
sed -i '/<policy domain=\"coder\" rights=\"none\" pattern=\"PDF\" \/>/d' /etc/ImageMagick-6/policy.xml
sed -i 's/rights="none"/rights="read|write"/g' /etc/ImageMagick-6/policy.xml
celery -A core worker --pool=solo