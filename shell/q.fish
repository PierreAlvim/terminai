function Q? --description 'Chat with AI to get shell commands'
    if contains -- --setup $argv
        python3 -m terminai.cli $argv
        return
    end
    set -l suggested_command (python3 -m terminai.cli $argv)
    if test -n "$suggested_command"
        commandline -rt "$suggested_command"
    end
end

function q? --description 'Alias for Q?'
    Q? $argv
end


