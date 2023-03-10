load('N.mat');
loc = xlsread('annTheft_Pop_Income.xls','loc');
load('validFoci.mat');
load('foci.mat');

numLGA = length(N);
% numYr = length(validFoci);
numYr = 10;
rF = zeros(numLGA,1);
%for yr = 1:numYr
for yr= 1:numYr
    for j = 1:length(validFoci{yr})
        ind = validFoci{yr}(j);
        rF(ind)=rF(ind)+1;
    end
end
r = find(rF >=ceil(numYr/5));
size(r);
r = sortrows([r rF(r)],-2); % 36 x 2 matrix with 36 validFoci and their count in decreasing order of the latter

xlswrite('refFoci.xls',r,'>=2yrsFullList');
refFoci = r(:,1); % First column of rF
save('refFoci.mat','refFoci')


for i = 1:length(r)
    rowNo = find(refFoci == r(i,1));
    if ~isempty(rowNo)
        n = N{r(i,1)};
        %Check neighbors of neighbors for CR
        temp = n;
        %for j = 1:length(n)
        %    temp = union(temp,N{n(j)}); % temp contains neighbors of ref foci: r(i,1) upto 2 levels
        %end
        n = setdiff(temp,r(i,1)); % eliminate the ref foci from the neighbours list

        [v ind]=intersect(refFoci,n); % find the list of nbhrs of ref foci r(i,1) that are also a ref foci
        %refFoci(setdiff(ind,1:rowNo)) = []; % set those refFoci's as null which are nbhrs of current foci and are yet to be processed
        refFoci(ind) = [];
    end
end
 

plot(loc(refFoci,1),loc(refFoci,2),'r*');
%loc(refFoci,:)
%xlswrite('refFoci.xls',[refFoci rF(refFoci)],'>=2yrs_r_2');

numFoci = length(refFoci) % = 16 for 10 years

% % %Consecutive Contiguous Foci ( CC )
ccInfo = cell(1,numFoci);  % 1 x 16 cells
ccFoci = cell(1,numFoci); % 1 x 16 cells
 
% % Foci within a radius ( CR )
crInfo = cell(1,numFoci);
crFoci = cell(1,numFoci);
% 
for i = 1:numFoci
    rF = refFoci(i);
    ccPrev = rF;
    ccInfo{i}= [(2001:2010)' zeros(10,2)];
    ccFoci{i}=[];

    crInfo{i} = [(2001:2010)' zeros(10,2)];
    crFoci{i}=[];
    for j = 1:numYr
        vF = validFoci{j};
        F = foci{j};
          
% %     % CC foci and info per year
        if ismember(ccPrev,vF)
            ccInfo{i}(j,2:3)= [ccPrev find(F==ccPrev)];
        else
            ccLoc = loc(ccPrev,:);
            n = N{ccPrev};
            I= intersect(vF,n);
            if ~isempty(I)
                ind = 1;
                if length(I) > 1
                    nLoc = loc(I,:);
                    ccDist = zeros(1,length(I));
                    for k = 1:length(I)
                        ccDist(k)=sqrt(realpow(ccLoc(1)-nLoc(k,1),2)+realpow(ccLoc(2)-nLoc(k,2),2));
                    end
                    [v ind]= min(ccDist);
                end
                ccInfo{i}(j,2:3)= [I(ind) find(F==I(ind))];
                ccPrev = I(ind);
            end
        end
        if isempty(ccFoci{i})
            ccFoci{i} = [ccFoci{i}; [ccInfo{i}(j,2) 1]];
        else
            rowNo = find(ccFoci{i}(:,1)==ccInfo{i}(j,2));
            if isempty(rowNo)
                ccFoci{i} = [ccFoci{i}; [ccInfo{i}(j,2) 1]];
            else
                ccFoci{i}(rowNo,2)= ccFoci{i}(rowNo,2)+1;
            end
        end
 
%       % CR foci and info per year
        if ismember(rF,vF)
            crInfo{i}(j,2:3)= [rF find(F==rF)];
        else
            crLoc = loc(rF,:);
            n = N{rF};             
%           %Check neighbors of neighbors for CR
            temp = n;
            for k = 1:length(n)
                temp = union(temp,N{n(k)});
            end
            n = setdiff(temp,rF);
            I= intersect(vF,n);
            if ~isempty(I)
                ind = 1;
                if length(I) > 1
                    nLoc = loc(I,:);
                    crDist = zeros(1,length(I));
                    for k = 1:length(I)
                        crDist(k)=sqrt(realpow(crLoc(1)-nLoc(k,1),2)+realpow(crLoc(2)-nLoc(k,2),2));
                    end
                    [v ind]= min(crDist);
                end
                crInfo{i}(j,2:3)= [I(ind) find(F==I(ind))];
            end
        end
        if isempty(crFoci{i})
            crFoci{i} = [crFoci{i}; [crInfo{i}(j,2) 1]];
        else
            rowNo = find(crFoci{i}(:,1)==crInfo{i}(j,2));
            if isempty(rowNo)
                crFoci{i} = [crFoci{i}; [crInfo{i}(j,2) 1]];
            else
                crFoci{i}(rowNo,2)= crFoci{i}(rowNo,2)+1;
            end
        end
      
    end
% %    xlswrite('CCInfo_fullList.xls',ccInfo{i},int2str(rF));
% %    xlswrite('CCFoci_fullList.xls',sortrows(ccFoci{i},-2),int2str(rF));
% %      xlswrite('CRInfo_fullList.xls',crInfo{i},int2str(rF));
% %      xlswrite('CRFoci_fullList.xls',sortrows(crFoci{i},-2),int2str(rF));
end
% % save('ccInfo.mat','ccInfo');
% % save('ccFoci.mat','ccFoci');
% save('crInfo.mat','crInfo');
% save('crFoci.mat','crFoci');
