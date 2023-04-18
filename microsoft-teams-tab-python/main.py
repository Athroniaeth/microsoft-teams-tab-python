import json
import os
import zipfile

from PIL import Image


def main():
    pass


import re


def create_microsoft_app_tab(
        site_url=None,
        developer_name=None,

        privacy_url=None,
        tou_url=None,

        tab_shortname='Tab',
        tab_fullname='PersonalTab',

        short_description="Short description here",
        full_description="Long description here",
        icon_outline='icon-outline.png',
        icon_color='icon-color.png',

        guid=None
):
    """
    Créer une application tab Microsoft Teams.

    site_url (str): L'URL du site que l'application va charger (doit commencer par 'https://').
    developer_name (str): Le nom du développeur.
    tab_shortname (str): Le nom court du tab (par défaut 'Tab').
    tab_fullname (str): Le nom complet du tab (par défaut 'PersonalTab').
    privacy_url (str): L'URL de la politique de confidentialité de l'application (par défaut site_url + '/privacy').
    tou_url (str): L'URL des conditions d'utilisation de l'application (par défaut site_url + '/tou').
    short_description (str): La description courte de l'application.
    full_description (str): La description complète de l'application.
    icon_outline (str): Le nom de l'image de l'icône de contour.
    icon_color (str): Le nom de l'image de l'icône de couleur.
    guid (str): L'id de l'application (format GUID), si non spécifié, un GUID aléatoire sera généré.
    """

    valid_image_extensions = ['.png', '.jpg', '.jpeg']

    assert site_url is not None, "Il faut que vous donniez une url 'https://' pour l'argument 'site_url',"
    assert re.match(r'^https://', site_url), "L'URL du site doit commencer par 'https://'"  # Vérifier L'URL du site

    assert os.path.exists(icon_color), f"Le fichier '{icon_color}' n'a pas été trouvé.."
    assert os.path.exists(icon_outline), f"Le fichier '{icon_outline}' n'a pas été trouvé.."

    _, ext = os.path.splitext(icon_color)
    assert ext.lower() in valid_image_extensions, f"Il faut que 'icon_color' soit un fichier avec une extension d'image '{icon_color}'"

    _, ext = os.path.splitext(icon_outline)
    assert ext.lower() in valid_image_extensions, f"Il faut que 'icon_color' soit un fichier avec une extension d'image '{icon_color}'"

    # Vérifier les dimensions de l'icône d'aperçu
    with Image.open(icon_color) as im:
        assert im.size == (192, 192), f"Il faut que l'image 'icon_outline' ai une taille de 192x192. L'image donnée fait '{im.size}'."

    # Vérifier les dimensions de l'icône de couleur
    with Image.open(icon_outline) as im:
        assert im.size == (32, 32), f"Il faut que l'image 'icon_color' ai une taille de 32x32. L'image donnée fait '{im.size}'."

    if developer_name is None:
        import getpass
        developer_name = getpass.getuser()
        print(f"Aucun nom de développeur n'a été donné pour l'argument 'developer_name', nous avons détecté l'utilisateur '{developer_name}' et celui ci à été choisi en nom de développeur.")

    if tab_shortname is None:
        tab_shortname = 'Tab'
        print(f"Aucun nom d'application court n'a été donné pour l'argument 'tab_shortname', Nous avons donc choisi le nom court par défaut : '{tab_shortname}'.")

    if tab_fullname is None:
        tab_fullname = 'PersonalTab'
        print(f"Aucun nom d'application complet n'a été donné pour l'argument 'tab_fullname', Nous avons donc choisi le nom court par défaut : '{tab_fullname}'.")

    if short_description is None:
        short_description = "Short description here"
        print(f"Aucune description d'application courte n'a été donné pour l'argument 'short_description', Nous avons donc choisi le nom court par défaut : '{short_description}'.")

    if full_description is None:
        full_description = "Long description here"
        print(f"Aucune description d'application complète n'a été donné pour l'argument 'full_description', Nous avons donc choisi la description complète par défaut : '{full_description}'.")

    # Générer un GUID aléatoire si nécessaire
    if not guid:
        guid = get_random_guid()
        print(f"Vous n'avez pas fournit d'argument 'guid', un guid aléatoire à été générer pour votre application : '{guid}'.")
    else:
        assert is_valid_teams_guid(guid), f"Le guid fournit ne respecte pas le format de guid imposé par Teams '{guid}'."

    # Définir les urls par défaut s'ils ne sont pas définis
    if not privacy_url:
        privacy_url = site_url + '/privacy'
        print(f"Vous n'avez pas fournit d'argument 'privacy_url' pour L'URL de la politique de confidentialité, nous avons donc déterminé que vous respecter le format Teams : '{privacy_url}'.")

    if not tou_url:
        tou_url = site_url + '/tou'
        print(f"Vous n'avez pas fournit d'argument 'tou_url pour L'URL des termes d'utilisations, nous avons donc déterminé que vous respecter le format Teams : '{tou_url}'.")


    # Créer le fichier zip
    zip_filename = tab_shortname + '.zip'

    # Il faut d'abord rajouter les images, au cas où que l'utilisateur donne un path, comme ça
    # nous n'avons plus qu'à modifier le path des images en noms d'images pour le manifest.json.
    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zip_file:

        # Ajouter les fichiers d'icône si existent dans le path
        if os.path.exists(icon_outline):
            zip_file.write(icon_outline)
            icon_outline = os.path.basename(icon_outline)

        if os.path.exists(icon_color):
            zip_file.write(icon_color)
            icon_color = os.path.basename(icon_color)

        # Créer le fichier manifest.json
        manifest = {

            "$schema": "https://developer.microsoft.com/en-us/json-schemas/teams/v1.12/MicrosoftTeams.schema.json",
            "manifestVersion": "1.12",
            "id": guid,
            "version": "1.0.0",
            "packageName": "com.custom.tab",
            "developer": {
                "name": developer_name,
                "websiteUrl": site_url,
                "privacyUrl": privacy_url,
                "termsOfUseUrl": tou_url,
                "mpnId": ""
            },
            "name": {
                "short": tab_shortname,
                "full": tab_fullname
            },
            "description": {
                "short": short_description,
                "full": full_description
            },
            "icons": {
                "outline": icon_outline,
                "color": icon_color
            },
            "accentColor": "#D85028",
            "configurableTabs": [],
            "staticTabs": [
                {
                    "entityId": "index",
                    "name": tab_fullname,
                    "contentUrl": site_url,
                    "websiteUrl": site_url,
                    "scopes": ["personal"]
                }
            ],
            "bots": [],
            "connectors": [],
            "composeExtensions": [],
            "permissions": [
                "identity",
                "messageTeamMembers"
            ],
            "validDomains": [site_url]}

        # Créer le fichier manifest.json dans le répertoire courant
        with open('manifest.json', 'w') as f:
            json.dump(manifest, f, indent=4)

        # Ajouter le fichier manifest.json
        zip_file.write('manifest.json')


    # Afficher un message de confirmation
    print(f"Le tab Microsoft Teams '{tab_shortname}' a été créé avec succès sous le nom de fichier '{zip_filename}'.")


def get_random_guid():
    """ Générer un GUID aléatoire. """
    import uuid
    return f"{uuid.uuid4()}"


def is_valid_teams_guid(guid):
    """ Vérifie si un GUID est un GUID Microsoft Teams valide. """
    import re
    pattern = r'^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-4[0-9a-fA-F]{3}-[8-9a-bA-B][0-9a-fA-F]{3}-[0-9a-fA-F]{12}$'
    return bool(re.match(pattern, guid))


if __name__ == '__main__':
    create_microsoft_app_tab('https://www.google.com')
