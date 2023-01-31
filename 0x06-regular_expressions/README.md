abc] 	A single character of: a, b, or c
[^abc] 	Any single character except: a, b, or c
[a-z] 	Any single character in the range a-z
[a-zA-Z] 	Any single character in the range a-z or A-Z
^ 	Start of line
$ 	End of line
\A 	Start of string
\z 	End of string
. 	Any single character
\s 	Any whitespace character
\S 	Any non-whitespace character
\d 	Any digit
\D 	Any non-digit
\w 	Any word character (letter, number, underscore)
\W 	Any non-word character
\b 	Any word boundary

* -file globe 
. - match any of 1 character

#!/usr/bin/env ruby
puts ARGV[0].scan(//).join
