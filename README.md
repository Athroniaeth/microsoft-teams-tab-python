
# Microsoft-Teams-Tab-Python

Bibliothèque python microscopique pour faciliter la création d'une application "tab" microsoft teams pour y mettre le site web que vous voulez.


## Lancer localement

Clone the project, and import microsoft-teams-tab-python and use the function 'create_microsoft_app_tab()'

```bash
  git clone https://github.com/Athroniaeth/microsoft-teams-tab-python.git
```


## Utilisation / Examples

```py
import microsoft-teams-tab-python

microsoft-teams-tab-python.create_microsoft_app_tab("https://www.google.com")
```


## API Reference

#### create_microsoft_app_tab()

Crée une application Microsoft Teams Tab en utilisant un site web et d'autres paramètres fournis.

| Paramètre           | Type      | Description                                                                                                       |
| ------------------ | --------- | ----------------------------------------------------------------------------------------------------------------- |
| `site_url`          | `str`     | **Obligatoire**. URL du site Web que l'application doit charger.                                                   |
| `guid`              | `str`     | **Obligatoire ou Aléatoire**. GUID unique de l'application.                                                                   |
| `developer_name`    | `str`     | **Obligatoire ou Detecté**. Nom du développeur de l'application.                                                             |
| `privacy_url`       | `str`     | URL facultative pour la politique de confidentialité de l'application. Par défaut, c'est l'URL du site + '/privacy'. |
| `terms_of_use_url`  | `str`     | URL facultative pour les conditions d'utilisation de l'application. Par défaut, c'est l'URL du site + '/tou'.      |
| `short_name`        | `str`     | Nom court facultatif de l'application. Par défaut, c'est "Tab".                                                   |
| `full_name`         | `str`     | Nom complet facultatif de l'application. Par défaut, c'est "PersonalTab".                                         |
| `short_description` | `str`     | Description courte facultative de l'application.                                                                 |
| `full_description`  | `str`     | Description complète facultative de l'application.                                                               |
| `icon_outline`      | `str`     | Nom de fichier facultatif pour l'icône d'aperçu de l'application.                                                 |
| `icon_color`        | `str`     | Nom de fichier facultatif pour l'icône de couleur de l'application.                                               |

Retourne le nom du fichier .zip créé pour l'application Microsoft Teams Tab.


## Screenshots

![Console Screenshot](https://github.com/Athroniaeth/microsoft-teams-tab-python/blob/main/images/console_screenshot.PNG)

![Zip Screenshot](https://github.com/Athroniaeth/microsoft-teams-tab-python/blob/main/images/zip_screenshot.PNG)

![Add Application Screenshot](https://github.com/Athroniaeth/microsoft-teams-tab-python/blob/main/images/add_application_screenshot.PNG)

![Application Screenshot](https://github.com/Athroniaeth/microsoft-teams-tab-python/blob/main/images/app_screenshot.PNG)
## License

[MIT](https://choosealicense.com/licenses/mit/)

