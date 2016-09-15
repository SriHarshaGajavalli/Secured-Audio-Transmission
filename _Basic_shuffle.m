clc
h=wavread('C:\Users\mural\Desktop\en.wav');
g=size(h);
p1=h(1:(g(1)/2),:);
p2=h((g(1)/2)+1:g(1),:);
en=vertcat(p2,p1);
s1=flipud(en);
audiowrite('de.wav' , s1 , 48000 );