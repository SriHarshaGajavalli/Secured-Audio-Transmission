
close all;
clear all;
clc;
 
% Configuration and connection
disp ('Receiver started');
t=tcpip('localhost', 4013,'NetworkRole','server');
 
% Wait for connection
disp('Waiting for connection');
fopen(t);
disp('Connection OK');
 
% Read data from the socket
h=[];
while true
    DataReceived=fread(t);
    y=str2mat(DataReceived')
    g=size(DataReceived);
    if g(1,2)==0
        break
    end
    h=[h,str2mat(DataReceived')];
        
end
h=textscan(h,'%s','delimiter',');')
h=h{1}
f=fopen('en.txt')
fprintf(f,'%s',h);
