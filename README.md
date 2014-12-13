pawl.github.io
==============

Resume for Paul Brown

Uses a customized version of the template from: https://github.com/prat0318/json_resume

Create a Ubuntu 14.04 droplet with Ruby On Rails already installed, then run the following commands:
```
apt-get install git
git clone https://github.com/pawl/pawl.github.io.git
cd pawl.github.io/
gem install json_resume
json_resume convert --template=template.mustache ./resume.json
json_resume convert --template=template.mustache --out=html_pdf ./resume.json
```
