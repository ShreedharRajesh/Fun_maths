clear
clc
close all

q1 = input('Enter Number of Pizzas in the oven at a time -: ');
x = zeros(q1,1);        %q1 Pizzas are put inside the oven
q2 = input('Enter Total number of Pizzas outside the oven -: ');
a = zeros(q2,1);
 for j = 1:q2           %Simulating the Random replacements of Pizzas and cooking times
     x = x+0.5;         %30 second increment
     r = randi([1 q1]); %Choosing a random pizza to take out
     a(j)=x(r);         %Labelling the cooking time for that pizza
     x(r)=0;            %Resetting the clock for that Pizza position
 end
 histogram(a,q2)        %Distribution plot
 xlabel ('Time taken for the Pizza to get cooked (Minutes)')
 ylabel ('Number of Pizzas cooked in the particular time interval')