#!/usr/bin/env ruby

def regex(arg)
  pattern = /[A-Z]+/
  matches = arg.scan(pattern)
  if matches.empty?
    puts ""
  else
    matches.each do |match|
      print match
    end
  end
  puts
end

regex(ARGV[0])
