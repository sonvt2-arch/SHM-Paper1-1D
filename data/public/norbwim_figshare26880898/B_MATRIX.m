function [B_mat] = B_MATRIX(N,k,Influence_Line,C_vec)

Inf_Line=Influence_Line;
B_Nrows=k;
B_Ncols=N;
C1_vec=C_vec;

B_mat=zeros(B_Nrows,B_Ncols);
L=1;

for j=1:length(Inf_Line)
    
    if L==1
        
        for i = 1:N
            for n=1:N
                B_mat(C1_vec(n)+i,n)=Inf_Line(j);
            end
        end
        L=L+1;
    
    elseif L>1
        
        for i = L:N+L
            for n=1:N
                B_mat(C1_vec(n)+i,n)=Inf_Line(j);
            end
        end
       L=L+1;
       
    end   
end

% if N>3
   [p q]=size(B_mat);
   B_mat=B_mat(1:p-N,1:N);
end
% end

