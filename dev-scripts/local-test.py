#!/usr/bin/env python3


from pathlib import Path

DEFAULT_REPLACEMENTS = {
    '__APP__': 'app_name',
    '__PATH__': '', # Same as "installed at domain root"
    '__DOMAIN__': '127.0.0.1',
    '__PORT__': '8000',
    #
    '__YNH_CURRENT_HOST__': 'localhost',
    #
    # config_panel.toml settings:
    '__DEBUG_ENABLED__': '0',  # "1" or "0" string
    '__LOG_LEVEL__': 'DEBUG',
    '__ADMIN_EMAIL__': 'admin-email@test.tld',
    '__DEFAULT_FROM_EMAIL__': 'default-from-email@test.tld',
}


def copy_patch(*, src_file, replaces, data_dir_path):
    print('_' * 100)
    print(f'IN...: {src_file}')
    dst_file = data_dir_path / src_file.name
    print(f'OUT..: {dst_file}')

    src_stat = src_file.stat()

    with src_file.open('r') as f:
        content = f.read()

    if replaces:
        for old, new in replaces.items():
            if old in content:
                print(f' * Replace "{old}" -> "{new}"')
                content = content.replace(old, new)

    with dst_file.open('w') as f:
        f.write(content)

    dst_file.chmod(mode=src_stat.st_mode)

    print()


def main():
    base_path = Path(__file__).parent.parent
    conf_path = base_path / 'conf'

    destination = base_path / 'local_test'

    data_dir_path = destination / 'home_yunohost_app'  # __DATA_DIR__ -> /home/yunohost.app/$app/
    data_dir_path.mkdir(parents=True, exist_ok=True)

    install_dir_path = destination / 'var_www_app'  # __INSTALL_DIR__ -> /var/www/$app/
    install_dir_path.mkdir(parents=True, exist_ok=True)

    REPLACES = {
        # New variable names, for "ynh_add_config" usage:
        '__DATA_DIR__': str(data_dir_path),  # e.g.: /home/yunohost.app/$app/
        '__INSTALL_DIR__': str(install_dir_path),  # e.g.: /var/www/$app/
        #
        **DEFAULT_REPLACEMENTS,
    }

    print('-' * 100)
    for file_path in sorted(conf_path.glob('*')):
        if not file_path.is_file():
            continue

        copy_patch(
            src_file=file_path,
            replaces=REPLACES,
            data_dir_path=data_dir_path,
        )
    print('-' * 100)


if __name__ == '__main__':
    main()
