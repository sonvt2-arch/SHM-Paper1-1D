function [A_mat] = A_MATRIX(N,k,C_vec,W)
Weights=W;
C1_vec=C_vec;
k1=k;
A_Nrows=k1;                      %% Total number of rows in matrix A
A_Ncols=k1-C1_vec(N);            %% Total number of cols in matrix A
A_mat=zeros(A_Nrows,A_Ncols);


for j=1:N
    L=1;
    for i = 1:A_Nrows
        A_mat(C1_vec(j)+i,i)=Weights(j);
        L=L+1;
        if L>A_Ncols
            break
        end
    end
end 

end

