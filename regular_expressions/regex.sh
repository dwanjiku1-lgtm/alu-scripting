#!/usr/bin/env bash

# Create directory
mkdir -p regular_expressions
cd regular_expressions || exit

# Task 1: Repetition Token #0 (matches hbttn, hbtttn, hbttttn, hbtttttn -> hbt{2,5}n)
cat << 'EOF' > 1-repetition_token_0.rb
#!/usr/bin/env ruby
puts ARGV[0].scan(/hbt{2,5}n/).join
EOF

# Task 2: Repetition Token #1 (matches htn, hbtn -> hb?tn)
cat << 'EOF' > 2-repetition_token_1.rb
#!/usr/bin/env ruby
puts ARGV[0].scan(/hb?tn/).join
EOF

# Task 3: Repetition Token #2 (matches hbtn, hbttn, hbtttn, ... -> hbt+n)
cat << 'EOF' > 3-repetition_token_2.rb
#!/usr/bin/env ruby
puts ARGV[0].scan(/hbt+n/).join
EOF

# Task 4: Repetition Token #3 (matches htn, hbtn, hbttn, ... without square brackets -> hbt*n or hb*tn)
cat << 'EOF' > 4-repetition_token_3.rb
#!/usr/bin/env ruby
puts ARGV[0].scan(/hbt*n/).join
EOF

# Task 5: Not quite HBTN yet (starts with h, ends with n, exactly 1 char in between -> ^h.n$)
cat << 'EOF' > 5-beginning_and_end.rb
#!/usr/bin/env ruby
puts ARGV[0].scan(/^h.n$/).join
EOF

# Task 6: Call me maybe (matches exactly a 10-digit phone number -> ^\d{10}$)
cat << 'EOF' > 6-phone_number.rb
#!/usr/bin/env ruby
puts ARGV[0].scan(/^\d{10}$/).join
EOF

# Task 7: OMG WHY ARE YOU SHOUTING? (matches only capital letters -> [A-Z])
cat << 'EOF' > 7-OMG_WHY_ARE_YOU_SHOUTING.rb
#!/usr/bin/env ruby
puts ARGV[0].scan(/[A-Z]/).join
EOF

# Task 8: Textme (extracts sender, receiver, and flags from log entries)
cat << 'EOF' > 8-textme.rb
#!/usr/bin/env ruby
from = ARGV[0].scan(/\[from:(.*?)\]/).join
to = ARGV[0].scan(/\[to:(.*?)\]/).join
flags = ARGV[0].scan(/\[flags:(.*?)\]/).join
puts "#{from},#{to},#{flags}"
EOF

# Make all created Ruby scripts executable
chmod +x *.rb

echo "All regular expression scripts have been successfully created and made executable!"
