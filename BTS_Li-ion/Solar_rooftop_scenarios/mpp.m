function mpp(voltage, current)
power = voltage.*current;
[max_power, i] = max(power);

v_max = voltage(i);
i_max = current(i);

%Plotting I-V
yyaxis left
plot(voltage, current, 'b');
hold on
plot(v_max, i_max, 'o')
ylabel('Current in amperes(A)', 'FontWeight', 'Bold', 'Color', 'k')

%Plotting P-V
yyaxis right
plot(voltage, power);
ylabel('Power in watts (W)', 'FontWeight', 'Bold', 'Color', 'k')

xlabel('Voltage in volts (V)', 'FontWeight', 'Bold', 'Color', 'k')

plot([v_max v_max], [0 max_power], '--r')
yyaxis left
plot([0 v_max],[i_max i_max], '--r')
text(v_max, i_max, 'Maximum Power Point')

end
