#!/usr/bin/env ruby

def reg_pattern(arg)
  patt = /^(?!hbtn).*$/
  comb_arg = arg.join(" ")

  matches = comb_arg.scan(patt)
  if matches.empty?
    puts ""
  else
    matches.each do |match|
      puts match
    end
  end
end

reg_pattern(ARGV)
