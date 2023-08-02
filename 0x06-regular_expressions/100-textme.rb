#!/usr/bin/env ruby

def reg_pattern(arg)
  pattern = /(from:|to:|flags:)(\w+|[+][0-9]*|[-].+-1)/x
  comb_arg = arg.join(' ')
  matches = comb_arg.scan(pattern)
  index = 0
  if matches.empty?
    puts ""
  else
    matches.each do |match|
      if index < match.length
        print match[1] + ','
        index += 1
      else
        print match[1]
      end
    end
  end
  puts
end


reg_pattern(ARGV)
