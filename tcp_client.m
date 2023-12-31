% matlab works as client, while Python works as server

open_system('MICRO_GRID_INF6103');
% start simulation and pause simulation, waiting for signal from python
set_param('MICRO_GRID_INF6103/var1', 'Value', num2str(1));
set_param('MICRO_GRID_INF6103/var2', 'Value', num2str(1));
set_param('MICRO_GRID_INF6103/var3', 'Value', num2str(1));
cmdk1 = 1;
cmdk2 = 1;
cmdk3 = 1;
set_param('MICRO_GRID_INF6103','SimulationCommand','start');

% open a client
t = tcpclient('127.0.0.1',9999);
all_data = [];
while(1)
    pause(2);
    % TCP sending
    u1 = out.tension1.data(1)
    u2 = out.intensite1.data(1)
    u3 = cmdk1;
	u4 = cmdk2;
	u5 = cmdk3;
    v = [u3,u4,u5,u1,u2];
    write(t,v);

    % TCP receiving
    while(1) % loop, until getting some data
        nBytes = get(t,'BytesAvailable');
        if nBytes > 0
            break;
        end
    end
    command_rev = read(t,nBytes); % read() will read binary as str
    data = str2num(char(command_rev)); % transform str into numerical matrix
    all_data = [all_data;data]; % store history data
    if isempty(data)
        data = [0,0,0,0,0];
    end
    tension1 = data(4);
    intensite1 = data(5);
    cmdk1 = data(1);
    cmdk2 = data(2); % separate each data in the matrix
	cmdk3 = data(3);
    % set parameter in the simulink model using the data from python
    % run the simulink model for one step
    set_param('MICRO_GRID_INF6103/var1', 'Value', num2str(cmdk1));
    set_param('MICRO_GRID_INF6103/var2', 'Value', num2str(cmdk2));
    set_param('MICRO_GRID_INF6103/var3', 'Value', num2str(cmdk3));
    set_param('MICRO_GRID_INF6103', 'SimulationCommand', 'step');
    set_param('MICRO_GRID_INF6103','SimulationCommand','update');


end

