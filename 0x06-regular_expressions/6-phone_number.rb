#!/usr/bin/env ruby

def reg_pattern(arg)
  pattern = /^\d+$/
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
reg_pattern(ARGV)
