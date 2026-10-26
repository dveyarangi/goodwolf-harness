#!/bin/sh
# Mechanism: mechanism-shape
# Every core hook runs here. Hosts launch through a Git alias:
#
#     git -c "alias.gw-hook=!sh .agents/scripts/gw/hook.sh" gw-hook <host>
#
# Git is on the path of every shell the hosts were seen to use — Git Bash, Windows PowerShell,
# cmd — and runs an alias under its own sh from the repository's top level, so one command serves
# every host and platform, from whatever folder the host's shell stands in. Git's pre-commit calls
# this wrapper directly from the work tree's root. The interpreter is the
# one the link step recorded in this clone's Git directory: a bare `python` may be the Windows
# Store stub, and `uv` is one machine's habit.

host="$1"
if [ "$host" = "pre-commit" ]; then
    # TODO q-0037.0006.0005.0001: each mechanism's records table will own these roots.
    # Git matches the roots without quoting or splitting a file's Unicode or newline characters.
    set --
    git diff --cached --quiet --no-renames -- docs/questions/ docs/tickets/ docs/rfc/ docs/sessions/ docs/product.md docs/edge/
    case $? in
        0) ;;
        1) set -- "$@" records ;;
        *) echo "refused: commit: cannot read the commit's files" >&2; exit 1 ;;
    esac
    git diff --cached --quiet --no-renames -- .agents/ docs/mechanisms/ AGENTS.md CLAUDE.md local.rules.md
    case $? in
        0) ;;
        1) set -- "$@" core ;;
        *) echo "refused: commit: cannot read the commit's files" >&2; exit 1 ;;
    esac
    [ "$#" -gt 0 ] || exit 0
fi
record=$(git rev-parse --git-path gw-interpreter 2>/dev/null)
python=""
if [ -n "$record" ] && [ -f "$record" ]; then
    python=$(head -n 1 "$record" | tr -d '\r')
fi
if [ -n "$python" ] && [ -f "$python" ]; then
    if [ "$host" = "pre-commit" ]; then
        exec "$python" .agents/scripts/gw/harness.py . --commit "$@"
    fi
    # The payload is kept whole for the store's hook; it is read here only to tell a session's
    # start, where the installer's check runs and its one line — a tree whose installed blocks
    # are out of step with its rules files and settings — is handed to the wake, which prints it
    # last in the host's own form. Nothing here may fail the host: a check that cannot run says
    # nothing.
    payload=$(mktemp 2>/dev/null || echo "${TMPDIR:-/tmp}/gw-hook-$$")
    cat > "$payload"
    notice=""
    if grep -qiE 'hook_event_name"[[:space:]]*:[[:space:]]*"sessionstart"' "$payload" 2>/dev/null \
        && [ -f .agents/scripts/gw/inject_rules.py ]; then
        notice=$("$python" .agents/scripts/gw/inject_rules.py --check --line 2>/dev/null)
    fi
    GW_NOTICE="$notice" "$python" .agents/scripts/gw/questions.py --hook "$host" < "$payload"
    status=$?
    rm -f "$payload"
    exit $status
fi

# No interpreter: say which step makes the record, in the form the host reads, and exit 0 — a
# failing prompt hook can hold back the person's message.
notice="This clone has no interpreter recorded for its hooks; run \`python .agents/scripts/gw/harness.py . --links\` once, on Windows with \`py -3\` for \`python\`, which may be the Store stub."
case "$host" in
    cursor) printf '{"additional_context": "%s"}\n' "$notice" ;;
    *) printf '%s\n' "$notice" ;;
esac
exit 0
