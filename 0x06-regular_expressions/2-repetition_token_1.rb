#!/usr/bin/env ruby

def regex_pattern(arg)
  pattern = /(hbtn|htn)/x
  comb_arg = arg.join(" ")
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
