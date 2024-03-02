# webbrowser_metrics_telegraf_plugin
Telegraph Plugin to collect webbrowser metrics

## Setup

### Install telegraf
```sh
cp telegraf/telegraf.conf /usr/local/etc/telegraf.conf
```

### Define Environment variables
```sh
DOCKER_INFLUXDB_INIT_HOST=localhost
DOCKER_INFLUXDB_INIT_ADMIN_TOKEN=qwerty
DOCKER_INFLUXDB_INIT_ORG=my-org
DOCKER_INFLUXDB_INIT_BUCKET=my-bucket
```

### Start telegraf

#### Start telegraf as a service
```sh
ln -sfv /usr/local/opt/telegraf/*.plist ~/Library/LaunchAgents
launchctl load ~/Library/LaunchAgents/homebrew.mxcl.telegraf.plist
```

#### Start telegraf as a standalone process
```sh
telegraf --config /usr/local/etc/telegraf.conf
```
