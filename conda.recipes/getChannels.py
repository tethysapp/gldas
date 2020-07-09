import yaml
try:
    with open("install.yml") as f:
        install_yml = yaml.safe_load(f)
        channels = install_yml.get('requirements').get('conda').get('channels')
        channelString = ""
        if "conda-forge" not in channels:
            channels.insert(0, "conda-forge")
        for channel in channels:
            channelString = channelString + " -c " + channel
        buildCommand = "conda build" + channelString + " --output-folder . ."
        print(buildCommand)
except Exception as e:
    # print(e)
    print("conda build -c conda-forge --output-folder . .")