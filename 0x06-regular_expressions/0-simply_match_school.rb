#!/usr/bin/env ruby

def regex_match(arguments)
  pattern = /School/
  combined_arguments = arguments.join("")

  matches = combined_arguments.scan(pattern)

  if matches.empty?
    print "" 
  else
    matches.each do |match|
      print match
    end
  end
  print "\n"
end

regex_match(ARGV)
