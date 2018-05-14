today=`date '+%Y_%m_%d__%H_%M_%S'`;
mkdir foo
mv shodan-* foo/
zip -r foo.zip foo
urll="https://transfer.sh/"$today".zip"
curl --upload-file foo.zip $urll ;echo
