import discord
import asyncio
import os
import sys
import getpass
from datetime import datetime

class UI:
    COLORS = {
        'reset': '\033[0m',
        'bold': '\033[1m',
        'dim': '\033[2m',
        'cyan': '\033[96m',
        'green': '\033[92m',
        'red': '\033[91m',
        'yellow': '\033[93m',
        'blue': '\033[94m',
        'magenta': '\033[95m',
        'gray': '\033[90m',
        'white': '\033[97m'
    }
    
    TRANSLATIONS = {
        'es': {
            'select_language': 'Seleccionar Idioma',
            'spanish': '🇪🇸 Español',
            'english': '🇺🇸 English',
            'choose': 'Elige una opción',
            'token_prompt': 'Token de Cuenta Discord',
            'token_missing': 'Token no proporcionado.',
            'connected': 'Conectado como',
            'servers': 'servidores',
            'main_menu': 'Menú Principal',
            'list_servers': 'Listar Servidores',
            'clone_server': 'Clonar Servidor',
            'back': '← Volver',
            'exit': 'Salir del Programa',
            'your_servers': 'Tus Servidores',
            'admin': 'ADMIN',
            'no_admin': 'sin admin',
            'members': 'Miembros',
            'clone_menu': 'Clonar Servidor',
            'select_source': 'Seleccionar servidor ORIGEN',
            'select_dest': 'Seleccionar servidor DESTINO',
            'or_enter_id': 'o ingresa el ID manualmente',
            'invalid_number': 'Número inválido. Intenta de nuevo.',
            'same_server_error': 'El servidor de origen y destino no pueden ser el mismo.',
            'source_not_found': 'Servidor origen no encontrado.',
            'dest_not_found': 'Servidor destino no encontrado.',
            'missing_perms': 'Faltan permisos en el servidor destino',
            'source': 'Origen',
            'dest': 'Destino',
            'warning_delete': 'ESTO ELIMINARÁ TODOS LOS CANALES Y ROLES DEL SERVIDOR DESTINO.',
            'confirm_clone': "¿Proceder? (escribe 'CLONAR' para confirmar)",
            'cancelled': 'Cancelado.',
            'cloning': 'Iniciando Clonado...',
            'updating_server': 'Actualizando nombre e icono...',
            'name_icon_changed': 'Nombre e icono cambiados.',
            'no_perm_name_icon': 'Sin permisos para cambiar nombre/icono.',
            'deleting_roles': 'Eliminando roles...',
            'role_deleted': 'Rol eliminado',
            'failed_delete_role': 'No se pudo eliminar el rol',
            'deleting_channels': 'Eliminando canales...',
            'channel_deleted': 'Canal eliminado',
            'failed_delete_channel': 'No se pudo eliminar el canal',
            'cloning_roles': 'Clonando roles...',
            'role_created': 'Rol creado',
            'failed_create_role': 'No se pudo crear el rol',
            'cloning_channels': 'Clonando canales...',
            'category_created': 'Categoría creada',
            'text_channel': 'Canal texto',
            'voice_channel': 'Canal voz',
            'clone_completed': 'CLONADO COMPLETADO',
            'roles_deleted': 'Roles eliminados',
            'channels_deleted': 'Canales eliminados',
            'channels_created': 'Canales creados',
            'total_time': 'Tiempo total',
            'seconds': 'segundos',
            'invalid_token': 'Token inválido.',
            'exiting': 'Saliendo...',
            'press_enter': 'Presiona Enter para continuar...'
        },
        'en': {
            'select_language': 'Select Language',
            'spanish': '🇪🇸 Español',
            'english': '🇺 English',
            'choose': 'Choose an option',
            'token_prompt': 'Discord Account Token',
            'token_missing': 'Token not provided.',
            'connected': 'Connected as',
            'servers': 'servers',
            'main_menu': 'Main Menu',
            'list_servers': 'List Servers',
            'clone_server': 'Clone Server',
            'back': '← Back',
            'exit': 'Exit Program',
            'your_servers': 'Your Servers',
            'admin': 'ADMIN',
            'no_admin': 'no admin',
            'members': 'Members',
            'clone_menu': 'Clone Server',
            'select_source': 'Select SOURCE server',
            'select_dest': 'Select DESTINATION server',
            'or_enter_id': 'or enter ID manually',
            'invalid_number': 'Invalid number. Try again.',
            'same_server_error': 'Source and destination cannot be the same.',
            'source_not_found': 'Source server not found.',
            'dest_not_found': 'Destination server not found.',
            'missing_perms': 'Missing permissions in destination server',
            'source': 'Source',
            'dest': 'Destination',
            'warning_delete': 'THIS WILL DELETE ALL CHANNELS AND ROLES FROM DESTINATION SERVER.',
            'confirm_clone': "Proceed? (type 'CLONE' to confirm)",
            'cancelled': 'Cancelled.',
            'cloning': 'Starting Clone...',
            'updating_server': 'Updating name and icon...',
            'name_icon_changed': 'Name and icon changed.',
            'no_perm_name_icon': 'No permission to change name/icon.',
            'deleting_roles': 'Deleting roles...',
            'role_deleted': 'Role deleted',
            'failed_delete_role': 'Could not delete role',
            'deleting_channels': 'Deleting channels...',
            'channel_deleted': 'Channel deleted',
            'failed_delete_channel': 'Could not delete channel',
            'cloning_roles': 'Cloning roles...',
            'role_created': 'Role created',
            'failed_create_role': 'Could not create role',
            'cloning_channels': 'Cloning channels...',
            'category_created': 'Category created',
            'text_channel': 'Text channel',
            'voice_channel': 'Voice channel',
            'clone_completed': 'CLONE COMPLETED',
            'roles_deleted': 'Roles deleted',
            'channels_deleted': 'Channels deleted',
            'channels_created': 'Channels created',
            'total_time': 'Total time',
            'seconds': 'seconds',
            'invalid_token': 'Invalid token.',
            'exiting': 'Exiting...',
            'press_enter': 'Press Enter to continue...'
        }
    }
    
    def __init__(self):
        self.lang = 'es'
    
    def t(self, key):
        return self.TRANSLATIONS[self.lang].get(key, key)
    
    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def banner(self):
        print(f"""
        {self.COLORS['magenta']}{self.COLORS['bold']}
        ██╗   ██╗██╗   ██╗███╗   ██╗ ██████╗
        ╚██╗ ██╔╝██║   ██║████╗  ██║██╔════╝
        ╚████╔╝ ██║   ██║██╔██╗ ██║██║  ███╗
        ╚██╔╝  ██║   ██║██║╚██╗██║██║   ██║
        ██║   ╚██████╔╝██║ ╚████║╚██████╝
        ╚═╝    ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝

        {self.COLORS['cyan']}Y U N G{self.COLORS['dim']}  •  by YvngxSanty
        {self.COLORS['yellow']}⚠ USE ONLY IN CONTROLLED ENVIRONMENTS ⚠{self.COLORS['reset']}
""")
    
    def language_menu(self):
        self.clear()
        print(f"\n{self.COLORS['cyan']}╔══════════════════════════════════════╗")
        print(f"║  {self.COLORS['bold']}{self.t('select_language').center(34)}{self.COLORS['reset']}{self.COLORS['cyan']}  ║")
        print(f"╠══════════════════════════════════════╣")
        print(f"║  {self.COLORS['green']}[1]{self.COLORS['reset']} {self.t('spanish')}                 {self.COLORS['cyan']}║")
        print(f"║  {self.COLORS['green']}[2]{self.COLORS['reset']} {self.t('english')}                  {self.COLORS['cyan']}║")
        print(f"╚══════════════════════════════════════╝{self.COLORS['reset']}\n")
        
        choice = input(f"{self.COLORS['magenta']}⟫ {self.COLORS['reset']}").strip()
        self.lang = 'en' if choice == '2' else 'es'
        self.clear()
    
    def log(self, msg, tipo="info"):
        hora = datetime.now().strftime("%H:%M:%S")
        iconos = {"ok": "✓", "error": "✗", "warn": "⚠", "info": "ℹ", "process": "⟳"}
        colores = {"ok": self.COLORS['green'], "error": self.COLORS['red'], 
                   "warn": self.COLORS['yellow'], "info": self.COLORS['cyan'], 
                   "process": self.COLORS['blue']}
        print(f"{colores.get(tipo, self.COLORS['reset'])}[{hora}] {iconos.get(tipo, '•')} {msg}{self.COLORS['reset']}")
    
    def header(self, text):
        print(f"\n{self.COLORS['cyan']}┌{'─' * 50}┐")
        print(f"│ {self.COLORS['bold']}{self.COLORS['white']}{text.center(48)}{self.COLORS['reset']}{self.COLORS['cyan']} │")
        print(f"└{'─' * 50}┘{self.COLORS['reset']}")
    
    def menu_option(self, num, text, color=None):
        if color is None:
            color = self.COLORS['green']
        print(f"  {color}[{num}]{self.COLORS['reset']} {text}")
    
    def menu(self, options, title):
        self.clear()
        self.banner()
        self.header(title)
        print()
        for num, text, color in options:
            self.menu_option(num, text, color)
        print()
    
    def success_box(self, lines):
        print(f"\n{self.COLORS['green']}┌{'─' * 50}┐")
        for line in lines:
            print(f"│ {self.COLORS['white']}{line.center(48)}{self.COLORS['reset']}{self.COLORS['green']} │")
        print(f"└{'─' * 50}┘{self.COLORS['reset']}\n")
    
    def input_prompt(self, text):
        return input(f"\n{self.COLORS['magenta']}⟫ {self.COLORS['white']}{text}: {self.COLORS['reset']}").strip()
    
    def wait_enter(self):
        input(f"\n{self.COLORS['dim']}{self.t('press_enter')}{self.COLORS['reset']}")

ui = UI()

class CloneBot(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.current_view = 'main'
    
    async def on_ready(self):
        ui.log(f"{ui.t('connected')}: {self.user} (ID: {self.user.id})", "ok")
        await self.main_menu()
    
    async def main_menu(self):
        self.current_view = 'main'
        options = [
            ('1', ui.t('list_servers'), ui.COLORS['cyan']),
            ('2', ui.t('clone_server'), ui.COLORS['magenta']),
            ('0', ui.t('exit'), ui.COLORS['red'])
        ]
        ui.menu(options, ui.t('main_menu'))
        
        choice = ui.input_prompt(ui.t('choose'))
        
        if choice == '1':
            await self.show_servers()
        elif choice == '2':
            await self.clone_server_menu()
        elif choice == '0':
            ui.log(ui.t('exiting'), "warn")
            await self.close()
            sys.exit(0)
        else:
            await self.main_menu()
    
    async def show_servers(self):
        self.current_view = 'servers'
        ui.clear()
        ui.banner()
        ui.header(ui.t('your_servers'))
        print()
        
        if not self.guilds:
            print(f"  {ui.COLORS['yellow']}No hay servidores disponibles.{ui.COLORS['reset']}\n")
        else:
            for i, guild in enumerate(self.guilds, 1):
                perms = f"{ui.COLORS['green']}{ui.t('admin')}{ui.COLORS['reset']}" if guild.me.guild_permissions.administrator else f"{ui.COLORS['gray']}{ui.t('no_admin')}{ui.COLORS['reset']}"
                print(f"  {ui.COLORS['cyan']}{i}.{ui.COLORS['reset']} {ui.COLORS['white']}{guild.name}{ui.COLORS['reset']}")
                print(f"     {ui.COLORS['dim']}ID: {guild.id} | {ui.t('members')}: {guild.member_count} | {perms}{ui.COLORS['reset']}")
                print()
        
        print(f"  {ui.COLORS['green']}[B]{ui.COLORS['reset']} {ui.t('back')}")
        print(f"  {ui.COLORS['red']}[0]{ui.COLORS['reset']} {ui.t('exit')}")
        
        choice = ui.input_prompt(ui.t('choose')).lower()
        
        if choice == 'b':
            await self.main_menu()
        elif choice == '0':
            ui.log(ui.t('exiting'), "warn")
            await self.close()
            sys.exit(0)
        else:
            await self.show_servers()
    
    async def clone_server_menu(self):
        ui.clear()
        ui.banner()
        ui.header(ui.t('clone_menu'))
        print()
        
        if not self.guilds:
            ui.log("No hay servidores disponibles para clonar.", "error")
            ui.wait_enter()
            await self.main_menu()
            return
        
        print(f"  {ui.COLORS['dim']}{'─' * 48}{ui.COLORS['reset']}")
        print(f"  {ui.COLORS['bold']}{ui.COLORS['white']}SERVIDORES DISPONIBLES:{ui.COLORS['reset']}")
        print(f"  {ui.COLORS['dim']}{'─' * 48}{ui.COLORS['reset']}")
        print()
        
        for i, guild in enumerate(self.guilds, 1):
            perms = f"{ui.COLORS['green']}✓ ADMIN{ui.COLORS['reset']}" if guild.me.guild_permissions.administrator else f"{ui.COLORS['red']}✗ {ui.t('no_admin')}{ui.COLORS['reset']}"
            print(f"  {ui.COLORS['cyan']}{i:2d}.{ui.COLORS['reset']} {ui.COLORS['white']}{guild.name[:35]:<35}{ui.COLORS['reset']} {perms}")
            print(f"      {ui.COLORS['dim']}ID: {guild.id}{ui.COLORS['reset']}")
            print()
        
        print(f"  {ui.COLORS['dim']}{'─' * 48}{ui.COLORS['reset']}")
        print(f"  {ui.COLORS['yellow']} {ui.t('or_enter_id')}{ui.COLORS['reset']}")
        print()
        
        print(f"\n{ui.COLORS['bold']}{ui.COLORS['magenta']}📤 {ui.t('select_source')}{ui.COLORS['reset']}")
        source_choice = ui.input_prompt("Número o ID")
        
        source_guild = self._resolve_server(source_choice)
        if not source_guild:
            ui.log(ui.t('source_not_found'), "error")
            ui.wait_enter()
            await self.main_menu()
            return
        
        print(f"\n{ui.COLORS['bold']}{ui.COLORS['cyan']}📥 {ui.t('select_dest')}{ui.COLORS['reset']}")
        dest_choice = ui.input_prompt("Número o ID")
        
        dest_guild = self._resolve_server(dest_choice)
        if not dest_guild:
            ui.log(ui.t('dest_not_found'), "error")
            ui.wait_enter()
            await self.main_menu()
            return
        
        if source_guild.id == dest_guild.id:
            ui.log(ui.t('same_server_error'), "error")
            ui.wait_enter()
            await self.main_menu()
            return
        
        dest_perms = dest_guild.me.guild_permissions
        required_perms = ['manage_roles', 'manage_channels', 'manage_guild']
        missing_perms = [p for p in required_perms if not getattr(dest_perms, p)]
        
        if missing_perms:
            ui.log(f"{ui.t('missing_perms')}: {', '.join(missing_perms)}", "error")
            ui.wait_enter()
            await self.main_menu()
            return
        
        print(f"\n{ui.COLORS['dim']}{'═' * 50}{ui.COLORS['reset']}")
        print(f"  {ui.COLORS['bold']}{ui.COLORS['white']}RESUMEN DE CLONADO:{ui.COLORS['reset']}")
        print(f"{ui.COLORS['dim']}{'═' * 50}{ui.COLORS['reset']}")
        print(f"\n  {ui.COLORS['magenta']} {ui.t('source')}:{ui.COLORS['reset']} {ui.COLORS['white']}{source_guild.name}{ui.COLORS['reset']}")
        print(f"     {ui.COLORS['dim']}ID: {source_guild.id}{ui.COLORS['reset']}")
        print(f"\n  {ui.COLORS['cyan']}📥 {ui.t('dest')}:{ui.COLORS['reset']} {ui.COLORS['white']}{dest_guild.name}{ui.COLORS['reset']}")
        print(f"     {ui.COLORS['dim']}ID: {dest_guild.id}{ui.COLORS['reset']}")
        print(f"\n{ui.COLORS['red']}{ui.COLORS['bold']}  ⚠ {ui.t('warning_delete')}{ui.COLORS['reset']}")
        print()
        
        confirm = ui.input_prompt(ui.t('confirm_clone'))
        if confirm.upper() not in ['CLONAR', 'CLONE']:
            ui.log(ui.t('cancelled'), "warn")
            ui.wait_enter()
            await self.main_menu()
            return
        
        await self.clone_guild(source_guild, dest_guild)
        ui.wait_enter()
        await self.main_menu()
    
    def _resolve_server(self, choice):
        try:
            num = int(choice)
            if 1 <= num <= len(self.guilds):
                return self.guilds[num - 1]
        except ValueError:
            pass
        
        try:
            guild_id = int(choice)
            return self.get_guild(guild_id)
        except ValueError:
            return None

    async def clone_guild(self, source, dest):
        ui.header(ui.t('cloning'))
        start_time = datetime.now()

        try:
            ui.log(ui.t('updating_server'), "process")
            try:
                icon_bytes = await source.icon.read() if source.icon else None
                await dest.edit(name=source.name, icon=icon_bytes, reason="Server cloning")
                ui.log(ui.t('name_icon_changed'), "ok")
            except Exception as e:
                ui.log(f"{ui.t('no_perm_name_icon')}: {e}", "warn")
            
            # Eliminar roles existentes (excepto @everyone y roles superiores)
            ui.log(ui.t('deleting_roles'), "process")
            roles_deleted = 0
            roles_to_delete = []
            
            # Obtener lista de roles a eliminar (excluyendo @everyone y roles por encima del bot)
            for role in dest.roles:
                if role.name == "@everyone":
                    continue
                if role >= dest.me.top_role:
                    ui.log(f"Rol '{role.name}' está por encima del bot - omitido", "warn")
                    continue
                roles_to_delete.append(role)
            
            # Eliminar roles de mayor a menor jerarquía (invertido)
            for role in reversed(roles_to_delete):
                try:
                    await role.delete(reason="Server cloning")
                    roles_deleted += 1
                    ui.log(f"{ui.t('role_deleted')}: {role.name}", "ok")
                except discord.Forbidden:
                    ui.log(f"{ui.t('failed_delete_role')} {role.name} - Sin permisos", "error")
                except Exception as e:
                    ui.log(f"{ui.t('failed_delete_role')} {role.name}: {e}", "error")
                await asyncio.sleep(0.3)
            
            ui.log(f"Total roles eliminados: {roles_deleted}", "ok")
            
            # Eliminar canales existentes
            ui.log(ui.t('deleting_channels'), "process")
            channels_deleted = 0
            for channel in list(dest.channels):
                try:
                    await channel.delete(reason="Server cloning")
                    channels_deleted += 1
                    ui.log(f"{ui.t('channel_deleted')}: {channel.name}", "ok")
                except discord.Forbidden:
                    ui.log(f"{ui.t('failed_delete_channel')} {channel.name} - Sin permisos", "warn")
                except Exception as e:
                    ui.log(f"{ui.t('failed_delete_channel')} {channel.name}: {e}", "error")
                await asyncio.sleep(0.3)
            
            ui.log(f"Total canales eliminados: {channels_deleted}", "ok")
            
            # Clonar roles del servidor origen
            ui.log(ui.t('cloning_roles'), "process")
            role_map = {}
            for role in reversed(source.roles):
                if role.name == "@everyone":
                    role_map[role.id] = dest.default_role
                    continue
                try:
                    new_role = await dest.create_role(
                        name=role.name, permissions=role.permissions,
                        colour=role.colour, hoist=role.hoist,
                        mentionable=role.mentionable, reason="Server cloning"
                    )
                    role_map[role.id] = new_role
                    ui.log(f"{ui.t('role_created')}: {role.name}", "ok")
                except Exception as e:
                    ui.log(f"{ui.t('failed_create_role')} {role.name}: {e}", "error")
                await asyncio.sleep(0.3)
            
            # Clonar categorías y canales
            ui.log(ui.t('cloning_channels'), "process")
            channels_created = 0
            category_map = {}
            
            for category in source.categories:
                try:
                    new_cat = await dest.create_category(name=category.name, reason="Server cloning")
                    category_map[category.id] = new_cat
                    ui.log(f"{ui.t('category_created')}: {category.name}", "ok")
                except Exception as e:
                    ui.log(f"Error en categoría {category.name}: {e}", "error")
                await asyncio.sleep(0.3)
            
            for channel in source.channels:
                if isinstance(channel, discord.CategoryChannel):
                    continue
                try:
                    overwrites = {}
                    for target, overwrite in channel.overwrites.items():
                        if isinstance(target, discord.Role) and target.id in role_map:
                            overwrites[role_map[target.id]] = overwrite
                    
                    category = category_map.get(channel.category_id) if channel.category_id else None
                    
                    if isinstance(channel, discord.TextChannel):
                        await dest.create_text_channel(
                            name=channel.name, category=category,
                            topic=channel.topic or "", slowmode_delay=channel.slowmode_delay,
                            nsfw=channel.nsfw, overwrites=overwrites, reason="Server cloning"
                        )
                        ui.log(f"{ui.t('text_channel')}: {channel.name}", "ok")
                    elif isinstance(channel, discord.VoiceChannel):
                        await dest.create_voice_channel(
                            name=channel.name, category=category,
                            bitrate=min(channel.bitrate, dest.bitrate_limit),
                            user_limit=channel.user_limit, overwrites=overwrites,
                            reason="Server cloning"
                        )
                        ui.log(f"{ui.t('voice_channel')}: {channel.name}", "ok")
                    channels_created += 1
                except Exception as e:
                    ui.log(f"Error en canal {channel.name}: {e}", "error")
                await asyncio.sleep(0.3)
            
            elapsed = (datetime.now() - start_time).total_seconds()
            ui.success_box([
                f"✅ {ui.t('clone_completed')}",
                f"📊 {ui.t('roles_deleted')}: {roles_deleted}",
                f"📊 {ui.t('channels_deleted')}: {channels_deleted}",
                f"📊 {ui.t('channels_created')}: {channels_created}",
                f"⏱️ {ui.t('total_time')}: {elapsed:.2f} {ui.t('seconds')}"
            ])
            
        except Exception as e:
            ui.log(f"Error fatal: {e}", "error")
            import traceback
            traceback.print_exc()

async def main():
    ui.language_menu()
    
    token = getpass.getpass(f"{ui.COLORS['magenta']}⟫ {ui.COLORS['white']}{ui.t('token_prompt')}: {ui.COLORS['reset']}").strip()
    if not token:
        ui.log(ui.t('token_missing'), "error")
        sys.exit(1)
    
    intents = discord.Intents.default()
    intents.guilds = True
    intents.members = True
    
    client = CloneBot(intents=intents)
    
    try:
        await client.start(token, bot=False)
    except discord.LoginFailure:
        ui.log(ui.t('invalid_token'), "error")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print(f"\n{ui.COLORS['yellow']} {ui.t('exiting')}{ui.COLORS['reset']}")