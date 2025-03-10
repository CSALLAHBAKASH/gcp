sudo apt-get update
sudo apt-get install git
sudo apt-get install gh


curl -sS https://webi.sh/gh | sh

gh auth login
gh api user -q ".login"
GITHUB_USERNAME=$(gh api user -q ".login")
git config --global user.name "${GITHUB_USERNAME}"
git config --global user.email "${USER_EMAIL}"
echo ${GITHUB_USERNAME}
echo ${USER_EMAIL}


cd ~
gh repo create  my_hugo_site --private 
gh repo clone  my_hugo_site 