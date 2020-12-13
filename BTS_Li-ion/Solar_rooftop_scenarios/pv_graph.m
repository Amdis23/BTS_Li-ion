for i = 1:3    
    subplot(3, 1, i)
    series = readtable('parallel_artificial.xlsx', 'ReadVariableNames', true, 'Sheet', i); 
    mpp(series.Voltage, series.Current)
    title('Parallel combination of 2 PV modules under artificial light - ')
    grid on
end


%  series = readtable('single_natural.xlsx', 'ReadVariableNames', true, 'Sheet', 1); 
%  mpp(series.Voltage, series.Current)
%  title('Single PV module under natural light')
%  grid on
