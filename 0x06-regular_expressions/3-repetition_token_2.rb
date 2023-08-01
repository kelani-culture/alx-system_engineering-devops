#!/usr/bin/env ruby

def reg_pattern(arg)
  patt = /hbt{1,4}n/x
  comb_arg = arg.join(" ")
  matched = comb_arg.scan(patt)

  if matched.empty?
    puts ""
  else
    matched.each do |match|
      puts match
    end
  end
end

reg_pattern(ARGV)
