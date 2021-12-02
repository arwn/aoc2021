x = 0
y = 0

File.open("input_2").each_line do |line|
    /(\w+)\s+(\d+)/ =~ line
    x += $2.to_i if $1 == 'forward'
    y -= $2.to_i if $1 == 'up'
    y += $2.to_i if $1 == 'down'
end

puts "x{#{x}} * y{#{y}} = #{x*y}"

# part 2

x = 0
aim = 0
y = 0

File.open("input_2").each_line do |line|
    /(\w+)\s+(\d+)/ =~ line
    if $1 == 'forward'
        x += $2.to_i 
        y += aim * $2.to_i
    elsif $1 == 'up'
        aim -= $2.to_i
    elsif$1 == 'down'
        aim += $2.to_i
    end
end

puts "x{#{x}} * y{#{y}} = #{x*y}"