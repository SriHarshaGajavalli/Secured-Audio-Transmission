% Clear console and workspace
clc;
clear all;
close all;
 
% Configuration and connection
t = tcpip('192.168.43.31',4013);
 
% Open socket and wait before sending data
fopen(t);
pause(0.2);
%%
%for i = 1:1:200
fileID = fopen(['C:\Users\mural\Desktop\en.txt'],'r');
message=textscan(fileID,'%s','Delimiter','\n');
fclose(fileID);
message=message{1};
message=cell2mat(message);
%%
% Send data every 500ms
 format long g;
 h=size(message);
for i=1:h(1,2) 
%message(1,i)
%o=bitxor(int32(message(i,1)),int32(7))
k=message(1,i);
   % DataToSend=message;
    fwrite(t,k);
  % pause (0.7);
end
end
%fwrite(t,condition);
% pause(0.5);
% Close and delete connection
fclose(t);
delete(t);