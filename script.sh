#!/bin/bash
tail -f \#fuckshit/out |  
while read foo ; do  
        if  echo $foo | grep "[0-9]\{4\}-[0-9]\{2\}-[0-9]\{2\} [0-9]\{2\}:[0-9]\{2\} <[^>]\+> iibot:"  ; then  
            name=$(echo $foo | awk '{print $3}' | sed 's,<\(.*\)>,\1,') ;
            message=$(echo $foo | cut -d ' ' -f5-) ;
            echo "/PRIVMSG #fuckshit :$name: FUCK YOUR FUCKING '$message'" > in ;
        fi;  
done
