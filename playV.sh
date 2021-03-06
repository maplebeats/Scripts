#!/bin/bash
#play videos with mplayer
#use anime.tm and anime.lst

temp_file=/tmp/playV.$$

video_time(){
    if [ ! -f ./anime.tm ];then
        echo -e "please input the period at the end of OP(Separated by Spaces)"
        read open_time_min open_time_sed
        if [[ $open_time_min == '' || $open_time_sed == '' ]];then
            echo "plase reput"
            read open_time_min open_time_sed
        fi
        open_time=`expr 60 \* $open_time_min + $open_time_sed`
        echo $open_time >anime.tm
        echo -e "please input the period at the open of ED(Separated by Spaces)"
        read end_time_min end_time_sed
        if [[ $end_time_min == '' || $end_time_sed == '' ]];then
            echo "please reput"
            read end_time_min end_time_sed
        fi
        end_time=`expr 60 \* $end_time_min + $end_time_sed - $open_time`
        echo $end_time >>anime.tm
        echo "the mplayer will play $open_time_min : $open_time_sed to $end_time_min : $end_time_sed"
    else
      n=0
      while read line
      do
          array[$n]=$line
          ((n++))
      done < anime.tm
      open_time=${array[0]}
      end_time=${array[1]}
  fi
}

creat_lst () {
    find . \( -name "*.rmvb" -or -name "*.mkv" \) -type f | vim -c 'sort nr /\d\+/' -c 'w '$temp_file'' -c 'q' - && cat $temp_file >anime.lst && rm $temp_file
    #find . \( -name "*.rmvb" \) -type f | sort > anime.lst
}

skip_open(){
    mplayer -fs -ss $open_time -playlist anime.lst >/dev/null 2>&1
}

skip_end(){
    killall sleep >/dev/null #防止多余的sleep影响
    sleep $end_time && killall mplayer >/dev/null 2>&1 && sed -i '1d' anime.lst && play_video >/dev/null
}

play_video(){
    if [ -s anime.lst ];then
        skip_end&
        skip_open
    else
        rm -f anime.lst
        echo "end of the videos!"
        exit 0
    fi
}

video_time
if [ -f ./anime.lst ]
then
    play_video
else
    creat_lst
    play_video
fi
