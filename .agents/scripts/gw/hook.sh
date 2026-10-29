#!/bin/sh
# Mechanism: mechanism-shape
# Every core hook runs here. A host's hooks are launched by a Git alias:
#
#     git -c "alias.gw-hook=!sh .agents/scripts/gw/hook.sh" gw-hook <host>
#
# Git is on the path of every shell the hosts were seen to use — Git Bash, Windows PowerShell,
# cmd — and runs an alias under its own sh from the repository's top level, so one command serves
# every host and platform, from whatever folder the host's shell stands in. Git's own `pre-push` is
# launched by the clone's hook file, `sh .agents/scripts/gw/hook.sh pre-push <remote> <url>`, from
# the same top level. The interpreter is the one the link step recorded in this clone's Git
# directory: a bare `python` may be the Windows Store stub, and `uv` is one machine's habit.
#
# The host branches never fail the host. The `pre-push` branch is the one that refuses by design:
# a push that carries a broken record of the method is stopped, and the checks say why.

host="$1"

interpreter() {
    # The worktree's own record, then the common directory's, so a push from a linked worktree is
    # checked under the clone's interpreter.
    for record in "$(git rev-parse --git-path gw-interpreter 2>/dev/null)" \
                  "$(git rev-parse --git-common-dir 2>/dev/null)/gw-interpreter"; do
        if [ -n "$record" ] && [ -f "$record" ]; then
            found=$(head -n 1 "$record" | tr -d '\r')
            if [ -n "$found" ] && [ -f "$found" ]; then
                printf '%s\n' "$found"
                return 0
            fi
        fi
    done
    return 1
}

if [ "$host" = "pre-push" ]; then
    # Git hands one line per ref: <local ref> <local sha> <remote ref> <remote sha>. No lines is
    # nothing sent; a deletion sends nothing. A push whose paths fall under none of the method's
    # roots starts no interpreter; a listing that fails wakes the checks, since what cannot be
    # listed is checked.
    # TODO q-0037.0006.0005.0001: the roots stand here and in harness.py until each mechanism's
    # table of its records carries them.
    remote="$2"
    refs=$(cat)
    [ -n "$refs" ] || exit 0
    roots='^"?(docs/|\.agents/|AGENTS\.md"?$|CLAUDE\.md"?$|local\.rules\.md"?$)'
    woken=""
    while read -r local_ref local_sha remote_ref remote_sha; do
        case "$local_sha" in *[!0]*) ;; *) continue ;; esac
        case "$remote_sha" in
            *[!0]*) paths=$(git -c core.quotepath=off diff --no-renames --name-only "$remote_sha" "$local_sha" 2>/dev/null) ;;
            *) paths=$(git -c core.quotepath=off log --root --no-renames --diff-merges=first-parent --name-only \
                   --format= "$local_sha" --not "--remotes${remote:+=$remote}" 2>/dev/null) ;;
        esac || { woken=1; break; }
        if printf '%s\n' "$paths" | grep -qE "$roots"; then
            woken=1
            break
        fi
    done <<EOF
$refs
EOF
    [ -n "$woken" ] || exit 0
    if ! python=$(interpreter); then
        printf '%s\n' "pre-push: this clone has no interpreter recorded, so the method's records go unchecked here; run \`python .agents/scripts/gw/harness.py . --links\` once." >&2
        exit 0
    fi
    printf '%s\n' "$refs" | "$python" .agents/scripts/gw/harness.py . --pre-push "$remote"
    exit $?
fi

record=$(git rev-parse --git-path gw-interpreter 2>/dev/null)
python=""
if [ -n "$record" ] && [ -f "$record" ]; then
    python=$(head -n 1 "$record" | tr -d '\r')
fi
if [ -n "$python" ] && [ -f "$python" ]; then
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
