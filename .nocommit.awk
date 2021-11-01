$1 == "#nocommit-begin", $1 == "#nocommit-end" { for ( i = 1; i <= NF; i++ ) { if ( i >= 2 ) $NF="" } } { print }
