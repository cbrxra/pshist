# PowerShell History CLI

![DEMO](.github\assets\demo.jpg)

PowerShell History is a Python-based CLI for tracking and managing PowerShell command history using profiles. It allows you to maintain separate command histories for different projects or environments, making it easier to organize and reuse your commands.

# Features

- Create profiles to keep separate command histories.
- Save or remove commands from profiles.
- Simple, fast, and easy to use.

# Commands

## Profile

Manage PowerShell history profiles.

### Create a profile

Creates a new profile.

```bash
pshist profile create <PROFILE>
```

**Example**

```bash
pshist profile create work
```

---

### Delete a profile

Deletes an existing profile.

```bash
pshist profile delete <PROFILE>
```

**Example**

```bash
pshist profile delete work
```

---

### Use a profile

Sets the active profile.

```bash
pshist profile use <PROFILE>
```

**Example**

```bash
pshist profile use work
```

---

### Exit the current profile

Stops using the current profile.

```bash
pshist profile exit
```

---

### List profiles

Displays all available profiles.

```bash
pshist profile list
```

---

### View a profile's history

Displays the stored command history of a profile.

```bash
pshist profile view <PROFILE>
```

**Example**

```bash
pshist profile view work
```

---

## History

Manage the history of the current profile.

### Add all pending commands

Imports all pending PowerShell commands into the current profile.

```bash
pshist history add all
```

---

### Add the last commands

Imports the last **N** PowerShell commands.

```bash
pshist history add last <N>
```

**Example**

```bash
pshist history add last 20
```

---

## Configuration

Manage application settings.

### Set the default profile

Sets the default profile.

```bash
pshist config set defaultprofile <PROFILE>
```

**Example**

```bash
pshist config set defaultprofile personal
```

---

### View all settings

Displays all configuration values.

```bash
pshist config view all
```

---

### View the default profile

Displays the current default profile.

```bash
pshist config view defaultprofile
```

---

## Version

Displays the installed version.

```bash
pshist --version
```

or

```bash
pshist -v
```