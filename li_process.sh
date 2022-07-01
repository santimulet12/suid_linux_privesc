#!/bin/bash

#en el caso de python
#import os
#os.system("chmod u+s /bin/bash")


old_process=$(ps -eo command)

while true
do
    new_process=$(ps -eo command)
    diff <(echo "$old_process") <(echo "$new_process") | grep "[\>\<]" | grep -v -E "li_process|command|kworker"
    old_process=$new_process
done