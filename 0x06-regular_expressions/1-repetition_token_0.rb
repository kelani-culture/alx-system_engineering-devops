#!/usr/bin/env ruby

def regex_pattern(argument)
  pattern = /hbt{2,5}n/x
  comb_arg = argument.join(" ")
  matches = comb_arg.scan(pattern)

  if matches.empty?
    puts ""
  else
    matches.each do |match|
      puts match
    end
  end
end
regex_pattern(ARGV)
